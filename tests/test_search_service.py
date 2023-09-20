
import unittest
from app.services.search_service import SearchService

class TestSearchService(unittest.TestCase):

    def setUp(self):
        self.search_service = SearchService()

    def test_search_upcoming_star_entrepreneurs(self):
        result = self.search_service.search_upcoming_star_entrepreneurs()
        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)

    def test_search_big_name_entrepreneurs(self):
        result = self.search_service.search_big_name_entrepreneurs()
        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)

if __name__ == '__main__':
    unittest.main()
