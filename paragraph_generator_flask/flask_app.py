import paragraph_generator as pg
from flask import Flask, jsonify, request
from werkzeug.exceptions import BadRequest

app = Flask(__name__)

VERBS = [
    {'verb': 'go', 'irregular_past': 'went', 'preposition': 'to', 'particle': '', 'objects': 1},
    {'verb': 'take', 'irregular_past': 'took', 'preposition': '', 'particle': 'away', 'objects': 1}
]
UNCOUNTABLE_NOUNS = [{'noun': 'water'}, {'noun': 'air'}]
COUNTABLE_NOUNS = [{'noun': 'dog', 'irregular_plural': ''}, {'noun': 'child', 'irregular_plural': 'children'}]
STATIC_NOUNS = [{'noun': 'Joe', 'is_plural': False}, {'noun': 'the two Jakes', 'is_plural': True}]


@app.route('/new')
def get_paragraph_json():
    json_data = request.json
    word_lists = pg.WordLists(verbs=VERBS, uncountable=UNCOUNTABLE_NOUNS, countable=COUNTABLE_NOUNS,
                              static=STATIC_NOUNS)

    answer, error = pg.ParagraphsGenerator({}, word_lists_generator=word_lists).generate_paragraphs()

    response = {'original_paragraph': pg.Serializer.to_json(answer),
                'display_str': str(error)}

    return jsonify(response)


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
