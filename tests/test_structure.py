# tests/test_structure.py
import unittest
import os
import yaml

class TestRepositoryStructure(unittest.TestCase):
    def setUp(self):
        self.root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

    def test_essential_files_exist(self):
        files = [
            "README.md",
            "CONTRIBUTING.md",
            "LICENSES.md",
            "LICENSE",
            "mkdocs.yml",
            "CITATION.cff",
            "docs/index.md",
            "docs/roadmap.md",
            "docs/principles.md",
            "docs/quality-gates.md",
            "docs/references/source-index.md",
            "docs/references/license-audit.md"
        ]
        for f in files:
            path = os.path.join(self.root, f)
            self.assertTrue(os.path.isfile(path), f"File {f} must exist.")

    def test_all_seasons_have_indexes(self):
        for s in [
            "01-computer-foundations",
            "02-software-engineering",
            "03-python-and-scientific-computing",
            "04-computer-architecture-gpu",
            "05-deep-learning-sciml",
            "06-llm-and-agents"
        ]:
            idx = os.path.join(self.root, "docs", "seasons", s, "index.md")
            self.assertTrue(os.path.isfile(idx), f"Season index {idx} must exist.")

    def test_mkdocs_config_validity(self):
        path = os.path.join(self.root, "mkdocs.yml")
        with open(path, encoding="utf-8") as f:
            data = yaml.safe_load(f)
            self.assertIn("site_name", data)
            self.assertIn("nav", data)

if __name__ == "__main__":
    unittest.main()
