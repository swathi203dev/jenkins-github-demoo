from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class WebsiteTests(unittest.TestCase):

    def test_homepage_exists(self):
        self.assertTrue((ROOT / "index.html").exists())

    def test_website_title(self):
        html = (ROOT / "index.html").read_text()
        self.assertIn("Swathi | DevOps Engineer", html)

    def test_technologies_exist(self):
        html = (ROOT / "index.html").read_text()

        for technology in ["Linux", "Jenkins", "Docker", "GitHub"]:
            self.assertIn(technology, html)

if __name__ == "__main__":
    unittest.main()