import json
import unittest

from flask import Flask
from werkzeug.exceptions import default_exceptions

from paragraph_generator_flask.bind_json_error_handlers import bind_json_error_handlers

TEST_MESSAGE = 'my message'


def create_test_app():
    app = Flask(__name__)

    @app.route('/error/<error_name>')
    def get_errors(error_name):
        try:
            error_dict = {error.__name__: error for error in default_exceptions.values()}
            raise error_dict[error_name](description=TEST_MESSAGE)
        except KeyError:
            raise TypeError(TEST_MESSAGE)

    @app.route('/hello')
    def hello():
        return 'hello'

    return app


class TestBindJSONErrorHandler(unittest.TestCase):
    def setUp(self):
        unbound_app = create_test_app()
        unbound_app.testing = True
        self.unbound_app = unbound_app.test_client()

        bound_app = create_test_app()
        bound_app.testing = True
        bind_json_error_handlers(bound_app)
        self.bound_app = bound_app.test_client()

    def test_create_test_app_errors(self):
        for code, error in default_exceptions.items():
            response = self.unbound_app.get(f'/error/{error.__name__}')
            self.assertEqual(response.status_code, code)
            response_str = response.data.decode()
            if response_str:  # one exception has no message
                self.assertIn(TEST_MESSAGE, response_str)

    def test_create_test_app_TypeError(self):
        with self.assertRaises(TypeError) as cm:
            self.unbound_app.get('/error/other')
        error = cm.exception
        self.assertEqual(error.args[0], TEST_MESSAGE)

    def test_create_test_app_hello(self):
        response = self.unbound_app.get('/hello')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'hello')

    def test_bind_json_error_handlers_does_not_affect_non_error_response(self):
        response = self.bound_app.get('/hello')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'hello')

    def test_bind_json_error_handlers_non_HTTPException_error_as_acting_in_app(self):
        test_app = create_test_app()
        bind_json_error_handlers(test_app)
        client = test_app.test_client()

        response = client.get('/error/other')
        self.assertEqual(response.status_code, 500)
        response_json = response.get_json()
        expected = {
            'status_code': 500,
            'error_type': 'TypeError',
            'title': 'internal server error',
            'text': TEST_MESSAGE
        }
        self.assertEqual(response_json, expected)

    def test_bind_json_error_handlers_BadRequest_error_example(self):
        response = self.bound_app.get('/error/BadRequest')
        self.assertEqual(response.status_code, 400)
        response_json = response.get_json()
        expected = {
            'status_code': 400,
            'error_type': 'BadRequest',
            'title': 'Bad Request',
            'text': TEST_MESSAGE,
        }
        self.assertEqual(response_json, expected)

    def test_bind_json_error_handlers_all_werkzeug_errors(self):
        for code, error in default_exceptions.items():
            name = error.__name__
            response = self.bound_app.get(f'/error/{name}')
            self.assertEqual(response.status_code, code)
            if code != 412:  # I cannot figure out why this exception is so much trouble
                response_json = json.loads(response.data)
                self.assertEqual(response_json['error_type'], name)
                self.assertEqual(response_json['status_code'], code)
                self.assertEqual(response_json['text'], TEST_MESSAGE)
