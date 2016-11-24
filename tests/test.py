# import sys
import os
import unittest
from fbbotw import fbbotw


class FbbotwTest(unittest.TestCase):

    def setUp(self):
        self.fbid = os.getenv('FBID', '')

    def test_typing(self):
        response = fbbotw.typing(fbid=self.fbid, sender_action="typing_on")
        self.assertTrue(response.json()['recipient_id'] == self.fbid)
        response = fbbotw.typing(fbid=self.fbid, sender_action="typing_off")
        self.assertTrue(response.json()['recipient_id'] == self.fbid)
        response = fbbotw.typing(fbid=self.fbid, sender_action="mark_seen")
        self.assertTrue(response.json()['recipient_id'] == self.fbid)


if __name__ == '__main__':
    unittest.main()