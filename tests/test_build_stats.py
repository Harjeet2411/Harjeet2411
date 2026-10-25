import json
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from build_stats import THEMES, languages_card, stats_card, summarize  # noqa: E402

FIXTURE = json.loads((Path(__file__).parent / "fixture.json").read_text())


def with_days(counts):
    user = json.loads(json.dumps(FIXTURE))
    days = [{"contributionCount": c, "date": f"d{i}"} for i, c in enumerate(counts)]
    user["contributionsCollection"]["contributionCalendar"]["weeks"] = [{"contributionDays": days}]
    return user


class SummarizeTests(unittest.TestCase):
    def test_commits_include_private_contributions(self):
        self.assertEqual(summarize(FIXTURE)["commits"], 560)

    def test_streak_ignores_an_empty_today(self):
        self.assertEqual(summarize(with_days([1, 0, 2, 3, 0]))["streak"], 2)
        self.assertEqual(summarize(with_days([1, 0, 2, 3, 4]))["streak"], 3)
        self.assertEqual(summarize(with_days([0, 0]))["streak"], 0)

    def test_languages_sorted_by_size_with_fallback_color(self):
        langs = summarize(FIXTURE)["languages"]
        self.assertEqual(langs[0][0], "Python")
        self.assertEqual(dict((n, c) for n, _, c in langs)["HCL"], "#8b949e")

    def test_cards_render_for_both_themes(self):
        s = summarize(FIXTURE)
        for t in THEMES.values():
            self.assertIn("812", stats_card(t, s))
            self.assertIn("Python", languages_card(t, s))


if __name__ == "__main__":
    unittest.main()
