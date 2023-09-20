
import unittest
from app.models.ai_agent import AIAgent

class TestAIAgent(unittest.TestCase):

    def setUp(self):
        self.ai_agent = AIAgent()

    def test_network_with_executives(self):
        result = self.ai_agent.network_with_executives()
        self.assertTrue(result)

    def test_schedule_meetings(self):
        result = self.ai_agent.schedule_meetings()
        self.assertTrue(result)

    def test_search_star_entrepreneurs(self):
        result = self.ai_agent.search_star_entrepreneurs()
        self.assertTrue(result)

    def test_find_big_name_entrepreneurs(self):
        result = self.ai_agent.find_big_name_entrepreneurs()
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
