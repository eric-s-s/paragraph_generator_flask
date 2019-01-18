import random
import unittest


from paragraph_generator import Paragraph

from paragraph_generator_flask import app
# from tests.mock_requests import MockRequests

HANDLER_PATCH_STR = 'zoo_keeper_server.flask_app.DBRequestHandler'
SESSION_PATCH_STR = 'zoo_keeper_server.data_base_session.DataBaseSession'


class TestFlaskApp(unittest.TestCase):

    def setUp(self):
        self.app = app.app.test_client()
        # self.session = TestSession()
        app.app.testing = True

    def test_get_with_empty_json(self):
        random.seed(374837)
        json_data = {}
        answer = self.app.get('/new', json=json_data)
        expected = {
            'original_paragraph': Paragraph([]),
            'display_string': 'a string',
        }
        answer_json = answer.get_json()
        self.assertEqual(expected, answer_json)

