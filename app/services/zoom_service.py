
import os
from zoomus import ZoomClient

class ZoomService:
    def __init__(self):
        self.client = ZoomClient(os.getenv('ZOOM_API_KEY'), os.getenv('ZOOM_API_SECRET'))

    def schedule_meeting(self, topic, start_time, duration, timezone='UTC'):
        response = self.client.meeting.create(
            user_id='me',
            topic=topic,
            type=2,
            start_time=start_time,
            duration=duration,
            timezone=timezone
        )
        return response

    def get_meeting_link(self, meeting_id):
        response = self.client.meeting.get(id=meeting_id)
        return response['join_url']
