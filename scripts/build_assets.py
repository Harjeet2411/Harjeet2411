"""Generate the profile README's SVG art in light and dark variants.

    python scripts/build_assets.py

Writes assets/<name>-dark.svg and assets/<name>-light.svg. The SVGs use system
fonts only because GitHub serves README images through a proxy that blocks
web-font requests.
"""

from __future__ import annotations

from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).resolve().parent.parent / "assets"

FONT = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
MONO = "ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace"

THEMES = {
    "dark": {
        "bg": "#0d1117",
        "panel": "#161b22",
        "border": "#30363d",
        "text": "#e6edf3",
        "muted": "#8b949e",
        "grid": "#1f2630",
        "a1": "#ff9900",  # AWS orange
        "a2": "#22d3ee",
        "ok": "#3fb950",
    },
    "light": {
        "bg": "#ffffff",
        "panel": "#f6f8fa",
        "border": "#d0d7de",
        "text": "#1f2328",
        "muted": "#59636e",
        "grid": "#eaeef2",
        "a1": "#d97706",
        "a2": "#0891b2",
        "ok": "#1a7f37",
    },
}


def svg(w: int, h: int, body: str, t: dict, title: str) -> str:
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{escape(title)}">
<title>{escape(title)}</title>
<defs>
  <linearGradient id="accent" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="{t['a1']}"/>
    <stop offset="1" stop-color="{t['a2']}"/>
  </linearGradient>
</defs>
<style>
  text {{ font-family: {FONT}; }}
  .mono {{ font-family: {MONO}; }}
  @media (prefers-reduced-motion: reduce) {{ * {{ animation: none !important; }} }}
</style>
{body}
</svg>
"""


def banner(t: dict) -> str:
    w, h = 1200, 320
    # Faint grid on the right, standing in for an infrastructure diagram.
    grid = "".join(
        f'<line x1="{x}" y1="0" x2="{x}" y2="{h}" stroke="{t["grid"]}"/>' for x in range(700, w, 40)
    ) + "".join(
        f'<line x1="700" y1="{y}" x2="{w}" y2="{y}" stroke="{t["grid"]}"/>' for y in range(0, h, 40)
    )
    # Small constellation of nodes: accounts wired to one control plane.
    hub = (960, 160)
    nodes = [(780, 70), (820, 250), (900, 40), (1040, 280), (1120, 90), (1150, 220), (870, 160), (1060, 30)]
    links = "".join(
        f'<line x1="{hub[0]}" y1="{hub[1]}" x2="{x}" y2="{y}" stroke="url(#accent)" stroke-opacity="0.55" stroke-width="1.5"/>'
        for x, y in nodes
    )
    dots = "".join(
        f'<circle cx="{x}" cy="{y}" r="6" fill="{t["panel"]}" stroke="{t["a2"]}" stroke-width="2">'
        f'<animate attributeName="r" values="6;8;6" dur="3s" begin="{i * 0.37:.2f}s" repeatCount="indefinite"/></circle>'
        for i, (x, y) in enumerate(nodes)
    )
    # Packets travelling from the hub out to each node.
    packets = "".join(
        f'<circle r="3" fill="{t["a1"]}"><animateMotion dur="{2.4 + (i % 3) * 0.5:.1f}s" begin="{i * 0.3:.1f}s" repeatCount="indefinite" '
        f'path="M{hub[0]},{hub[1]} L{x},{y}"/></circle>'
        for i, (x, y) in enumerate(nodes)
    )
    body = f"""
<rect width="{w}" height="{h}" rx="16" fill="{t['bg']}" stroke="{t['border']}"/>
<g opacity="0.9">{grid}</g>
{links}{packets}{dots}
<circle cx="{hub[0]}" cy="{hub[1]}" r="26" fill="{t['panel']}" stroke="url(#accent)" stroke-width="3"/>
<text x="{hub[0]}" y="{hub[1] + 6}" text-anchor="middle" font-size="16" font-weight="700" fill="{t['text']}">AWS</text>
<rect x="56" y="64" width="64" height="6" rx="3" fill="url(#accent)"/>
<text x="56" y="140" font-size="62" font-weight="800" fill="{t['text']}">Harjeet J L</text>
<text x="58" y="186" font-size="26" font-weight="600" fill="url(#accent)">Cloud Engineer · DevOps &amp; CloudOps</text>
<text x="58" y="226" font-size="19" fill="{t['muted']}">Shipping AWS infrastructure and CI/CD at KFin Technologies</text>
<text x="58" y="268" class="mono" font-size="16" fill="{t['muted']}">$ terraform apply<tspan fill="{t['ok']}">  ✓ 44 accounts</tspan><tspan fill="{t['text']}"> ▍<animate attributeName="opacity" values="1;0;1" dur="1.1s" repeatCount="indefinite"/></tspan></text>
"""
    return svg(w, h, body, t, "Harjeet J L, Cloud Engineer, DevOps and CloudOps")


def impact(t: dict) -> str:
    stats = [
        ("2,000+", "production deployments", "shipped on AWS"),
        ("44", "AWS accounts", "across multiple regions"),
        ("6h → 5–7m", "build + deploy time", "after Jenkins + Terraform"),
        ("42k+", "resources", "in the largest account"),
    ]
    w, h, gap = 1200, 170, 20
    cw = (w - gap * 3) / 4
    cards = ""
    for i, (big, label, sub) in enumerate(stats):
        x = i * (cw + gap)
        cards += f"""
<g>
  <rect x="{x + 1}" y="1" width="{cw - 2}" height="{h - 2}" rx="14" fill="{t['panel']}" stroke="{t['border']}"/>
  <rect x="{x + 24}" y="26" width="36" height="4" rx="2" fill="url(#accent)"/>
  <text x="{x + 24}" y="86" font-size="40" font-weight="800" fill="{t['text']}">{escape(big)}
    <animate attributeName="opacity" from="0" to="1" dur="0.8s" begin="{i * 0.2:.1f}s" fill="freeze"/></text>
  <text x="{x + 24}" y="120" font-size="18" font-weight="600" fill="{t['text']}">{escape(label)}</text>
  <text x="{x + 24}" y="146" font-size="15" fill="{t['muted']}">{escape(sub)}</text>
</g>"""
    return svg(w, h, cards, t, "Impact: 2,000+ production deployments, 44 AWS accounts, build and deploy cut from 6 hours to minutes, 42k+ resources")


def pipeline(t: dict) -> str:
    stages = [
        ("git push", "Gitea"),
        ("test", "Jenkins"),
        ("build", "Docker"),
        ("provision", "Terraform"),
        ("deploy", "ECS · EKS"),
        ("verify", "health checks"),
    ]
    w, h = 1200, 150
    n = len(stages)
    bw, gap = 160, (w - 160 * n) / (n - 1)
    y = 40
    parts = []
    for i, (verb, tool) in enumerate(stages):
        x = i * (bw + gap)
        done = i == n - 1
        parts.append(f"""
<rect x="{x + 1}" y="{y}" width="{bw - 2}" height="76" rx="12" fill="{t['panel']}" stroke="{t['ok'] if done else t['border']}" stroke-width="{2 if done else 1}"/>
<text x="{x + bw / 2}" y="{y + 32}" text-anchor="middle" class="mono" font-size="16" font-weight="700" fill="{t['text']}">{escape(verb)}</text>
<text x="{x + bw / 2}" y="{y + 56}" text-anchor="middle" font-size="14" fill="{t['muted']}">{escape(tool)}</text>""")
        if i < n - 1:
            x1, x2 = x + bw + 6, x + bw + gap - 6
            parts.append(
                f'<line x1="{x1}" y1="{y + 38}" x2="{x2}" y2="{y + 38}" stroke="url(#accent)" stroke-width="2" stroke-dasharray="4 4">'
                f'<animate attributeName="stroke-dashoffset" from="16" to="0" dur="0.8s" repeatCount="indefinite"/></line>'
            )
    parts.append(
        f'<circle r="5" fill="{t["a1"]}"><animateMotion dur="6s" repeatCount="indefinite" path="M{bw / 2},{y + 38} L{w - bw / 2},{y + 38}"/></circle>'
    )
    parts.append(
        f'<text x="{w / 2}" y="{h - 6}" text-anchor="middle" font-size="14" fill="{t["muted"]}">one push → healthy service in minutes, no hand-edited YAML or .tf files</text>'
    )
    return svg(w, h, "".join(parts), t, "Release pipeline: git push, test, build, provision, deploy, verify")


def project_card(t: dict, title: str, stack: str, lines: list[str], tag: str) -> str:
    w, h = 590, 230
    body = f"""
<rect x="1" y="1" width="{w - 2}" height="{h - 2}" rx="14" fill="{t['panel']}" stroke="{t['border']}"/>
<rect x="1" y="1" width="{w - 2}" height="6" rx="3" fill="url(#accent)"/>
<text x="28" y="56" font-size="24" font-weight="800" fill="{t['text']}">{escape(title)}</text>
<rect x="{w - 28 - len(tag) * 8.2 - 20}" y="34" width="{len(tag) * 8.2 + 20}" height="28" rx="14" fill="none" stroke="{t['border']}"/>
<text x="{w - 28 - (len(tag) * 8.2 + 20) / 2}" y="53" text-anchor="middle" font-size="13" fill="{t['muted']}">{escape(tag)}</text>
<text x="28" y="88" class="mono" font-size="14" fill="{t['a2']}">{escape(stack)}</text>
"""
    for i, line in enumerate(lines):
        yy = 126 + i * 28
        body += (
            f'<circle cx="34" cy="{yy - 5}" r="3" fill="{t["a1"]}"/>'
            f'<text x="48" y="{yy}" font-size="16" fill="{t["text"]}">{escape(line)}</text>'
        )
    return svg(w, h, body, t, f"{title}: {stack}")


PROJECTS = {
    "buildforge": dict(
        title="BuildForge",
        stack="Java · Python · MCP AI agent · Jenkins",
        tag="internal",
        lines=[
            "Explains every failed Jenkins build: root cause",
            "and fix shown right under the failing stage",
            "Incident log, Teams alerts, time-to-fix dashboard",
            "No Jenkinsfile changes needed",
        ],
    ),
    "waf-platform": dict(
        title="Centralized WAF Monitoring",
        stack="Lambda · Step Functions · FastAPI · ECS Fargate",
        tag="internal",
        lines=[
            "Watches AWS WAF activity across 44 accounts",
            "Every change is simulated, approved, executed,",
            "verified and audited",
            "RDS PostgreSQL backend, Python throughout",
        ],
    ),
}


def main() -> None:
    OUT.mkdir(exist_ok=True)
    for name, t in THEMES.items():
        files = {
            "banner": banner(t),
            "impact": impact(t),
            "pipeline": pipeline(t),
            **{f"project-{k}": project_card(t, **v) for k, v in PROJECTS.items()},
        }
        for base, content in files.items():
            (OUT / f"{base}-{name}.svg").write_text(content, encoding="utf-8")
    print(f"wrote {len(list(OUT.glob('*.svg')))} files to {OUT}")


if __name__ == "__main__":
    main()
