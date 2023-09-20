
from app.main import create_app
import unittest

app = create_app()

class TestRun(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True 

    def test_home_status_code(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)

if __name__ == "__main__":
    unittest.main()
