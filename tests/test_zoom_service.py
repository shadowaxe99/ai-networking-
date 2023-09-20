
import unittest
from app.services.zoom_service import ZoomService

class TestZoomService(unittest.TestCase):

    def setUp(self):
        self.zoom_service = ZoomService()

    def test_schedule_meeting(self):
        result = self.zoom_service.schedule_meeting("test@example.com", "2022-12-31 12:00:00")
        self.assertIsNotNone(result)

    def test_cancel_meeting(self):
        result = self.zoom_service.cancel_meeting("test@example.com", "123456789")
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
