
import unittest
from app.services.email_service import EmailService

class TestEmailService(unittest.TestCase):

    def setUp(self):
        self.email_service = EmailService()

    def test_send_email(self):
        result = self.email_service.send_email("test@example.com", "Test Subject", "Test Body")
        self.assertTrue(result)

    def test_find_email(self):
        result = self.email_service.find_email("Elon Musk")
        self.assertEqual(result, "elonmusk@example.com")

if __name__ == '__main__':
    unittest.main()
