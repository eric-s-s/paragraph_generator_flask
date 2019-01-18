
from flask import Flask, jsonify, request
from werkzeug.exceptions import BadRequest

app = Flask(__name__)


@app.route('/')
def get_paragraph_json():
    json_data = request.json
    return jsonify(json_data)


def _get_json() -> dict:
    """
    :raise: BadRequest
    :rtype: dict
    :return: JSON as dict
    """
    try:
        return request.get_json()
    except BadRequest:
        msg = "This here is we call a fucked-up JSON: {}".format(request.data)
        raise BadRequest(msg)


if __name__ == '__main__':
    app.run()
