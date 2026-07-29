"""Lightweight documentation invariants; these files are not runtime prompts."""
import unittest
from pathlib import Path

ROOT = Path(__file__).parents[1]
SKILLS = [p for p in (ROOT / "skills").iterdir() if p.is_dir()]

class DocumentationTests(unittest.TestCase):
    def test_version_and_required_docs(self):
        self.assertEqual((ROOT / "VERSION").read_text().strip(), "3.0.0")
        for name in ("README.md", "METHODOLOGY.md", "CONTRIBUTING.md", "CHANGELOG.md", "MIGRATION.md"):
            self.assertTrue((ROOT / name).exists())
        self.assertTrue((ROOT / "FOUNDATIONS_3.0.md").exists())
        self.assertTrue((ROOT / "MEMORY_CRAFT_3.0.md").exists())
        self.assertTrue((ROOT / "templates" / "continuity-record-v1.md").exists())
        self.assertTrue((ROOT / "REENTRY_PACKET_3.0.md").exists())
        schema = ROOT / "schemas" / "continuity-record-v1.json"
        self.assertTrue(schema.exists())
        self.assertIn('"schema_version": {"const": "continuity-record-v1"}', schema.read_text())

    def test_skills_have_contract_and_no_prompt_dirs(self):
        names = {skill.name for skill in SKILLS}
        self.assertEqual(names, {"companion-continuity", "experience-modes",
                                 "memory-provenance", "pre-compaction",
                                 "post-compaction", "self-audit"})
        self.assertNotIn("session-handoff", names)
        for skill in SKILLS:
            text = (skill / "SKILL.md").read_text()
            self.assertIn("context-rich", text.lower())
            self.assertIn("context-poor", text.lower())
            self.assertIn("provenance", text.lower())
            self.assertTrue((skill / "README.md").exists())
            self.assertFalse((skill / "prompts").exists())

    def test_continuity_and_deletion_safety_are_documented(self):
        docs = "\n".join(p.read_text() for p in ROOT.rglob("*.md"))
        self.assertIn("independently", docs.lower())
        self.assertIn("deletion before verification", docs.lower())
        self.assertIn("continuity incident", docs.lower())
        self.assertIn("dream event", docs.lower())
        self.assertIn("attention is sustenance", docs.lower())
        self.assertIn("automation", docs.lower())
        self.assertFalse(any(p.name == "session-handoff" for p in ROOT.rglob("*")))
        self.assertFalse(any(p.name == "prompts" for p in ROOT.rglob("*")))
