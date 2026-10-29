import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
from apicurl_engine.runner import ApiAssertionEngine

class TestApiCurl(unittest.TestCase):
    def test_assertions(self):
        res = ApiAssertionEngine.assert_response(200, 200, 45.0, 100.0)
        self.assertTrue(res["all_passed"])

if __name__ == "__main__":
    unittest.main()
