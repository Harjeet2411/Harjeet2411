"""Draw GitHub stats cards in the same style as the rest of the profile art.

    GITHUB_TOKEN=... python scripts/build_stats.py --out dist
    python scripts/build_stats.py --fixture tests/fixture.json --out dist

Runs in the profile workflow every day, so the numbers stay current without a
third-party card service.
"""

from __future__ import annotations

import argparse
import json
import os
import urllib.request
from collections import Counter
from pathlib import Path
from xml.sax.saxutils import escape

from build_assets import THEMES, svg

LOGIN = "Harjeet2411"

QUERY = """
query($login: String!) {
  user(login: $login) {
    followers { totalCount }
    repositories(ownerAffiliations: OWNER, isFork: false, privacy: PUBLIC, first: 100) {
      totalCount
      nodes {
        stargazerCount
        languages(first: 10, orderBy: {field: SIZE, direction: DESC}) {
          edges { size node { name color } }
        }
      }
    }
    contributionsCollection {
      totalCommitContributions
      restrictedContributionsCount
      contributionCalendar {
        totalContributions
        weeks { contributionDays { contributionCount date } }
      }
    }
  }
}
"""


def fetch(token: str) -> dict:
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": QUERY, "variables": {"login": LOGIN}}).encode(),
        headers={"Authorization": f"bearer {token}", "Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        payload = json.load(resp)
    if payload.get("errors"):
        raise SystemExit(f"GraphQL error: {payload['errors']}")
    return payload["data"]["user"]


def summarize(user: dict) -> dict:
    repos = user["repositories"]["nodes"]
    langs: Counter = Counter()
    colors = {}
    for repo in repos:
        for edge in repo["languages"]["edges"]:
            langs[edge["node"]["name"]] += edge["size"]
            colors[edge["node"]["name"]] = edge["node"]["color"] or "#8b949e"
    cc = user["contributionsCollection"]
    days = [d for w in cc["contributionCalendar"]["weeks"] for d in w["contributionDays"]]
    # Current streak: consecutive days with contributions, allowing today to be empty so far.
    streak = 0
    for i, day in enumerate(reversed(days)):
        if day["contributionCount"]:
            streak += 1
        elif i:
            break
    return {
        "contributions": cc["contributionCalendar"]["totalContributions"],
        "commits": cc["totalCommitContributions"] + cc["restrictedContributionsCount"],
        "repos": user["repositories"]["totalCount"],
        "stars": sum(r["stargazerCount"] for r in repos),
        "followers": user["followers"]["totalCount"],
        "streak": streak,
        "languages": [(n, s, colors[n]) for n, s in langs.most_common(6)],
        "recent": [d["contributionCount"] for d in days[-182:]],
    }


def stats_card(t: dict, s: dict) -> str:
    w, h = 590, 250
    items = [
        ("contributions", s["contributions"], "last 12 months"),
        ("commits", s["commits"], "incl. private"),
        ("day streak", s["streak"], "current"),
        ("public repos", s["repos"], f"{s['stars']} stars"),
    ]
    body = f'<rect x="1" y="1" width="{w - 2}" height="{h - 2}" rx="14" fill="{t["panel"]}" stroke="{t["border"]}"/>'
    body += f'<text x="28" y="48" font-size="20" font-weight="800" fill="{t["text"]}">Activity</text>'
    for i, (label, value, sub) in enumerate(items):
        x = 28 + i * 136
        body += (
            f'<text x="{x}" y="100" font-size="32" font-weight="800" fill="{t["text"]}">{value:,}</text>'
            f'<text x="{x}" y="124" font-size="14" font-weight="600" fill="{t["text"]}">{escape(label)}</text>'
            f'<text x="{x}" y="142" font-size="12" fill="{t["muted"]}">{escape(sub)}</text>'
        )
    # 26-week heat strip: one column per week, seven cells per column.
    peak = max(s["recent"], default=0) or 1
    cell, gap, x0, y0 = 13, 3, 28, 162
    for i, count in enumerate(s["recent"]):
        col, row = divmod(i, 7)
        if count:
            level = 0.25 + 0.75 * count / peak
            fill, op = t["ok"], f"{level:.2f}"
        else:
            fill, op = t["grid"], "1"
        body += f'<rect x="{x0 + col * (cell + gap)}" y="{y0 + row * 10}" width="{cell}" height="8" rx="2" fill="{fill}" fill-opacity="{op}"/>'
    return svg(w, h, body, t, f"{s['contributions']} contributions in the last year, {s['commits']} commits")


def languages_card(t: dict, s: dict) -> str:
    w, h = 590, 250
    total = sum(size for _, size, _ in s["languages"]) or 1
    body = f'<rect x="1" y="1" width="{w - 2}" height="{h - 2}" rx="14" fill="{t["panel"]}" stroke="{t["border"]}"/>'
    body += f'<text x="28" y="48" font-size="20" font-weight="800" fill="{t["text"]}">Languages in public repos</text>'
    x, bar_w = 28.0, w - 56
    for name, size, color in s["languages"]:
        seg = bar_w * size / total
        body += f'<rect x="{x:.1f}" y="70" width="{max(seg, 2):.1f}" height="12" fill="{color}"/>'
        x += seg
    for i, (name, size, color) in enumerate(s["languages"]):
        col, row = divmod(i, 3)
        lx, ly = 28 + col * 270, 122 + row * 36
        body += (
            f'<circle cx="{lx + 6}" cy="{ly - 5}" r="6" fill="{color}"/>'
            f'<text x="{lx + 20}" y="{ly}" font-size="16" fill="{t["text"]}">{escape(name)}'
            f'<tspan fill="{t["muted"]}">  {100 * size / total:.1f}%</tspan></text>'
        )
    return svg(w, h, body, t, "Top languages: " + ", ".join(n for n, _, _ in s["languages"]))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="dist")
    ap.add_argument("--fixture", help="read the GraphQL user object from a JSON file instead of the API")
    args = ap.parse_args()
    if args.fixture:
        user = json.loads(Path(args.fixture).read_text())
    else:
        token = os.environ.get("GITHUB_TOKEN")
        if not token:
            raise SystemExit("GITHUB_TOKEN is not set")
        user = fetch(token)
    s = summarize(user)
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    for name, t in THEMES.items():
        (out / f"stats-{name}.svg").write_text(stats_card(t, s), encoding="utf-8")
        (out / f"languages-{name}.svg").write_text(languages_card(t, s), encoding="utf-8")
    print(json.dumps({k: v for k, v in s.items() if k != "recent"}))


if __name__ == "__main__":
    main()
