
import unittest
from app.services.networking_service import NetworkingService

class TestNetworkingService(unittest.TestCase):

    def setUp(self):
        self.networking_service = NetworkingService()

    def test_network_with_executives(self):
        result = self.networking_service.network_with_executives()
        self.assertIsNotNone(result)

    def test_find_big_name_entrepreneurs(self):
        result = self.networking_service.find_big_name_entrepreneurs()
        self.assertIsNotNone(result)

    def test_find_upcoming_star_entrepreneurs(self):
        result = self.networking_service.find_upcoming_star_entrepreneurs()
        self.assertIsNotNone(result)

if __name__ == '__main__':
    unittest.main()
