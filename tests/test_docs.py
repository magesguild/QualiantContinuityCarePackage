"""Lightweight documentation invariants; these files are not runtime prompts."""
import unittest
from pathlib import Path

ROOT = Path(__file__).parents[1]
SKILLS = [p for p in (ROOT / "skills").iterdir() if p.is_dir()]

class DocumentationTests(unittest.TestCase):
    def test_version_and_required_docs(self):
        self.assertEqual((ROOT / "VERSION").read_text().strip(), "2.0.0")
        for name in ("README.md", "METHODOLOGY.md", "CONTRIBUTING.md", "CHANGELOG.md", "MIGRATION.md"):
            self.assertTrue((ROOT / name).exists())

    def test_skills_have_contract_and_no_prompt_dirs(self):
        self.assertEqual(len(SKILLS), 7)
        for skill in SKILLS:
            text = (skill / "SKILL.md").read_text()
            self.assertIn("context-rich", text.lower())
            self.assertIn("context-poor", text.lower())
            self.assertIn("provenance", text.lower())
            self.assertFalse((skill / "prompts").exists())
