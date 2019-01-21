from flask import jsonify
from werkzeug.exceptions import HTTPException, default_exceptions


def bind_json_error_handlers(app):
    for code, error in default_exceptions.items():
        app.errorhandler(code)(handle_error)


def handle_error(error):
    error_type = error.__class__.__name__

    if not isinstance(error, HTTPException):
        title = 'internal server error'
        text = error.args[0]
        status_code = 500
    else:
        title = error.name
        text = error.description
        status_code = error.code
    response_json = {
        'title': title,
        'status_code': status_code,
        'text': text,
        'error_type': error_type
    }
    response = jsonify(response_json)
    response.status_code = status_code

    return response
