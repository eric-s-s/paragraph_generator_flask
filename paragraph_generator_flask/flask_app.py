import paragraph_generator as pg
from flask import Flask, jsonify, request
from werkzeug.exceptions import BadRequest

app = Flask(__name__)


@app.route('/generate')
def get_paragraph_json():
    json_data = request.json
    word_lists = json_data['word_lists']
    word_lists = pg.WordLists(
        verbs=word_lists['verb_groups'],
        uncountable=word_lists['uncountable_nouns'],
        countable=word_lists['countable_nouns'],
        static=word_lists['static_nouns'])

    answer, error = pg.ParagraphsGenerator(json_data['config'], word_lists_generator=word_lists).generate_paragraphs()

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
