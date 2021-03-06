import paragraph_generator as pg
from bind_json_error_handlers import bind_json_error_handlers
from flask import Flask, jsonify, request


def create_app():
    app = Flask(__name__)
    bind_json_error_handlers(app)

    @app.route('/generate')
    def get_paragraph_json():
        json_data = request.get_json()
        word_lists = json_data['word_lists']
        word_lists = pg.WordLists(
            verbs=word_lists['verb_groups'],
            uncountable=word_lists['uncountable_nouns'],
            countable=word_lists['countable_nouns'],
            static=word_lists['static_nouns'])

        answer, error = pg.ParagraphsGenerator(json_data['config'],
                                               word_lists_generator=word_lists).generate_paragraphs()

        response = {'original_paragraph': pg.Serializer.to_json(answer),
                    'display_str': str(error)}

        return jsonify(response)

    @app.route('/query/<query_type>')
    def query(query_type):
        json_data = request.get_json()
        submission_str = json_data['submission_str']
        original_paragraph_json = json_data['original_paragraph']
        checker = _get_checker(submission_str, original_paragraph_json)

        methods = {
            'is_correct': checker.is_submission_correct,
            'count_word_errors': checker.count_word_errors,
            'count_sentence_errors': checker.count_sentence_errors,
            'word_hints': checker.get_word_hints,
            'sentence_hints': checker.get_sentence_hints,
        }

        base_response = methods[query_type]()

        response = _format_response(base_response, query_type)

        return jsonify(response)

    def _get_checker(submission_str, original_paragraph_json):
        paragraph = pg.Serializer.from_json(original_paragraph_json)
        checker = pg.AnswerChecker(submission_str, paragraph)
        return checker

    def _format_response(base_response, query_type):
        if isinstance(base_response, dict):
            return _change_keys(base_response, query_type)

        responses = {
            'is_correct': {'is_correct': base_response},
            'count_word_errors': {'word_errors': base_response},
            'count_sentence_errors': {'sentence_errors': base_response},
        }
        return responses[query_type]

    def _change_keys(base_response, query_type):
        new_key = 'sentence_errors' if 'sentence' in query_type else 'word_errors'
        new_response = {key: val for key, val in base_response.items() if key != 'error_count'}
        new_response[new_key] = base_response['error_count']
        return new_response

    return app


if __name__ == '__main__':
    create_app().run()
