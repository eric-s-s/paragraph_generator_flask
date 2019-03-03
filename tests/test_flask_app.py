import json
import random
import unittest

from paragraph_generator import Serializer, Paragraph, Sentence, Noun, Verb, Punctuation

from paragraph_generator_flask import flask_app

VERBS = [
    {'verb': 'go', 'irregular_past': 'went', 'preposition': 'to', 'particle': '', 'objects': 1},
    {'verb': 'take', 'irregular_past': 'took', 'preposition': '', 'particle': 'away', 'objects': 1}
]
UNCOUNTABLE_NOUNS = [{'noun': 'water', 'definite': False}, {'noun': 'air', 'definite': True}]
COUNTABLE_NOUNS = [{'noun': 'dog', 'irregular_plural': ''}, {'noun': 'child', 'irregular_plural': 'children'}]
STATIC_NOUNS = [{'noun': 'Joe', 'is_plural': False}, {'noun': 'the two Jakes', 'is_plural': True}]


class TestFlaskApp(unittest.TestCase):

    def setUp(self):
        test_app = flask_app.create_app()
        test_app.testing = True
        self.app = test_app.test_client()
        self.verb_groups = VERBS
        self.countable_nouns = COUNTABLE_NOUNS
        self.uncountable_nouns = UNCOUNTABLE_NOUNS
        self.static_nouns = STATIC_NOUNS

        self.word_lists = {'verb_groups': self.verb_groups,
                           'uncountable_nouns': self.uncountable_nouns,
                           'countable_nouns': self.countable_nouns,
                           'static_nouns': self.static_nouns}

    def test_generate_with_empty_config_json(self):
        random.seed(374837)
        config_json = {}
        json_data = {
            'config': config_json,
            'word_lists': self.word_lists
        }
        answer = self.app.get('/generate', json=json_data)
        expected = {
            'display_str': "Children go to the two Jakes, the two Jakes take us away. The Joe takes away the air. The air takes away the two Jakes. The two Jakes take away the children. Child don't take him away. They take away water! Water goes to the the two Jakes. The two Jakes go to water! Waters doesn't take away the air, an air go to the children! The children take away a dog. The dog doesn't go to him. He went to an air, the air goes to them,",
            'original_paragraph': '{"class": "Paragraph", "sentence_list": [{"class": "Sentence", "word_list": [{"class": "Noun", "tags": ["PLURAL"], "value": "Children", "irregular_plural": "children", "base_noun": "child"}, {"class": "Verb", "tags": [], "value": "go", "irregular_past": "went", "infinitive": "go"}, {"class": "BasicWord", "tags": ["PREPOSITION"], "value": "to"}, {"class": "Noun", "tags": ["PLURAL", "PROPER"], "value": "the two Jakes", "irregular_plural": "", "base_noun": "the two Jakes"}, {"class": "Punctuation", "name": "EXCLAMATION"}]}, {"class": "Sentence", "word_list": [{"class": "Noun", "tags": ["PLURAL", "PROPER"], "value": "The two Jakes", "irregular_plural": "", "base_noun": "the two Jakes"}, {"class": "Verb", "tags": [], "value": "take", "irregular_past": "took", "infinitive": "take"}, {"class": "Pronoun", "name": "US"}, {"class": "BasicWord", "tags": ["SEPARABLE_PARTICLE"], "value": "away"}, {"class": "Punctuation", "name": "PERIOD"}]}, {"class": "Sentence", "word_list": [{"class": "Noun", "tags": ["PROPER"], "value": "Joe", "irregular_plural": "", "base_noun": "Joe"}, {"class": "Verb", "tags": ["THIRD_PERSON"], "value": "takes", "irregular_past": "took", "infinitive": "take"}, {"class": "BasicWord", "tags": ["SEPARABLE_PARTICLE"], "value": "away"}, {"class": "Noun", "tags": ["UNCOUNTABLE", "DEFINITE"], "value": "the air", "irregular_plural": "", "base_noun": "air"}, {"class": "Punctuation", "name": "PERIOD"}]}, {"class": "Sentence", "word_list": [{"class": "Noun", "tags": ["UNCOUNTABLE", "DEFINITE"], "value": "The air", "irregular_plural": "", "base_noun": "air"}, {"class": "Verb", "tags": ["THIRD_PERSON"], "value": "takes", "irregular_past": "took", "infinitive": "take"}, {"class": "BasicWord", "tags": ["SEPARABLE_PARTICLE"], "value": "away"}, {"class": "Noun", "tags": ["PLURAL", "PROPER"], "value": "the two Jakes", "irregular_plural": "", "base_noun": "the two Jakes"}, {"class": "Punctuation", "name": "PERIOD"}]}, {"class": "Sentence", "word_list": [{"class": "Noun", "tags": ["PLURAL", "PROPER"], "value": "The two Jakes", "irregular_plural": "", "base_noun": "the two Jakes"}, {"class": "Verb", "tags": [], "value": "take", "irregular_past": "took", "infinitive": "take"}, {"class": "BasicWord", "tags": ["SEPARABLE_PARTICLE"], "value": "away"}, {"class": "Noun", "tags": ["PLURAL", "DEFINITE"], "value": "the children", "irregular_plural": "children", "base_noun": "child"}, {"class": "Punctuation", "name": "PERIOD"}]}, {"class": "Sentence", "word_list": [{"class": "Noun", "tags": ["PLURAL", "DEFINITE"], "value": "The children", "irregular_plural": "children", "base_noun": "child"}, {"class": "Verb", "tags": ["NEGATIVE"], "value": "don\'t take", "irregular_past": "took", "infinitive": "take"}, {"class": "Pronoun", "name": "HIM"}, {"class": "BasicWord", "tags": ["SEPARABLE_PARTICLE"], "value": "away"}, {"class": "Punctuation", "name": "PERIOD"}]}, {"class": "Sentence", "word_list": [{"class": "CapitalPronoun", "name": "THEY"}, {"class": "Verb", "tags": [], "value": "take", "irregular_past": "took", "infinitive": "take"}, {"class": "BasicWord", "tags": ["SEPARABLE_PARTICLE"], "value": "away"}, {"class": "Noun", "tags": ["UNCOUNTABLE"], "value": "water", "irregular_plural": "", "base_noun": "water"}, {"class": "Punctuation", "name": "EXCLAMATION"}]}, {"class": "Sentence", "word_list": [{"class": "Noun", "tags": ["UNCOUNTABLE"], "value": "Water", "irregular_plural": "", "base_noun": "water"}, {"class": "Verb", "tags": ["THIRD_PERSON"], "value": "goes", "irregular_past": "went", "infinitive": "go"}, {"class": "BasicWord", "tags": ["PREPOSITION"], "value": "to"}, {"class": "Noun", "tags": ["PLURAL", "PROPER"], "value": "the two Jakes", "irregular_plural": "", "base_noun": "the two Jakes"}, {"class": "Punctuation", "name": "PERIOD"}]}, {"class": "Sentence", "word_list": [{"class": "Noun", "tags": ["PLURAL", "PROPER"], "value": "The two Jakes", "irregular_plural": "", "base_noun": "the two Jakes"}, {"class": "Verb", "tags": [], "value": "go", "irregular_past": "went", "infinitive": "go"}, {"class": "BasicWord", "tags": ["PREPOSITION"], "value": "to"}, {"class": "Noun", "tags": ["UNCOUNTABLE"], "value": "water", "irregular_plural": "", "base_noun": "water"}, {"class": "Punctuation", "name": "EXCLAMATION"}]}, {"class": "Sentence", "word_list": [{"class": "Noun", "tags": ["UNCOUNTABLE"], "value": "Water", "irregular_plural": "", "base_noun": "water"}, {"class": "Verb", "tags": ["THIRD_PERSON", "NEGATIVE"], "value": "doesn\'t take", "irregular_past": "took", "infinitive": "take"}, {"class": "BasicWord", "tags": ["SEPARABLE_PARTICLE"], "value": "away"}, {"class": "Noun", "tags": ["UNCOUNTABLE", "DEFINITE"], "value": "the air", "irregular_plural": "", "base_noun": "air"}, {"class": "Punctuation", "name": "PERIOD"}]}, {"class": "Sentence", "word_list": [{"class": "Noun", "tags": ["UNCOUNTABLE", "DEFINITE"], "value": "The air", "irregular_plural": "", "base_noun": "air"}, {"class": "Verb", "tags": ["THIRD_PERSON"], "value": "goes", "irregular_past": "went", "infinitive": "go"}, {"class": "BasicWord", "tags": ["PREPOSITION"], "value": "to"}, {"class": "Noun", "tags": ["PLURAL", "DEFINITE"], "value": "the children", "irregular_plural": "children", "base_noun": "child"}, {"class": "Punctuation", "name": "EXCLAMATION"}]}, {"class": "Sentence", "word_list": [{"class": "Noun", "tags": ["PLURAL", "DEFINITE"], "value": "The children", "irregular_plural": "children", "base_noun": "child"}, {"class": "Verb", "tags": [], "value": "take", "irregular_past": "took", "infinitive": "take"}, {"class": "BasicWord", "tags": ["SEPARABLE_PARTICLE"], "value": "away"}, {"class": "Noun", "tags": ["INDEFINITE"], "value": "a dog", "irregular_plural": "", "base_noun": "dog"}, {"class": "Punctuation", "name": "PERIOD"}]}, {"class": "Sentence", "word_list": [{"class": "Noun", "tags": ["DEFINITE"], "value": "The dog", "irregular_plural": "", "base_noun": "dog"}, {"class": "Verb", "tags": ["THIRD_PERSON", "NEGATIVE"], "value": "doesn\'t go", "irregular_past": "went", "infinitive": "go"}, {"class": "BasicWord", "tags": ["PREPOSITION"], "value": "to"}, {"class": "Pronoun", "name": "HIM"}, {"class": "Punctuation", "name": "PERIOD"}]}, {"class": "Sentence", "word_list": [{"class": "CapitalPronoun", "name": "HE"}, {"class": "Verb", "tags": ["THIRD_PERSON"], "value": "goes", "irregular_past": "went", "infinitive": "go"}, {"class": "BasicWord", "tags": ["PREPOSITION"], "value": "to"}, {"class": "Noun", "tags": ["UNCOUNTABLE", "DEFINITE"], "value": "the air", "irregular_plural": "", "base_noun": "air"}, {"class": "Punctuation", "name": "PERIOD"}]}, {"class": "Sentence", "word_list": [{"class": "Noun", "tags": ["UNCOUNTABLE", "DEFINITE"], "value": "The air", "irregular_plural": "", "base_noun": "air"}, {"class": "Verb", "tags": ["THIRD_PERSON"], "value": "goes", "irregular_past": "went", "infinitive": "go"}, {"class": "BasicWord", "tags": ["PREPOSITION"], "value": "to"}, {"class": "Pronoun", "name": "THEM"}, {"class": "Punctuation", "name": "EXCLAMATION"}]}], "tags": ["HAS_PLURALS", "HAS_NEGATIVES", "SIMPLE_PRESENT"]}'
        }
        answer_json = answer.get_json()
        self.assertEqual(expected, answer_json)

    def test_generate_with_config_json(self):
        config = {
            'error_probability': 0.0,
            'tense': 'simple_past',
            'probability_pronoun': 1.0,
            'probability_negative_verb': 1.0,
            'paragraph_size': 1
        }
        json_data = {
            'config': config,
            'word_lists': self.word_lists
        }
        answer = self.app.get('/generate', json=json_data)
        display_str = answer.get_json()['display_str']

        self.assertIn("didn't", display_str)

        expected_starts = ["I", "You", "He", "She", "It", "We", "They"]
        self.assertTrue(any(display_str.startswith(pronoun) for pronoun in expected_starts))

        expected_ends = ['me', 'you', 'him', 'her', 'it', 'us', 'them']
        self.assertTrue(any(pronoun in display_str for pronoun in expected_ends))

        punctuation_count = display_str.count('.') + display_str.count('!')
        self.assertEqual(punctuation_count, 1)

    def test_generate_original_paragraph_is_properly_serialized_as_answer_paragraph(self):
        config = {
            'error_probability': 0.0,
        }
        json_data = {
            'config': config,
            'word_lists': self.word_lists
        }
        answer_json = self.app.get('/generate', json=json_data).get_json()
        paragraph_obj = Serializer.from_json(answer_json['original_paragraph'])
        self.assertEqual(str(paragraph_obj), answer_json['display_str'])

    def test_generate_verb_groups(self):
        verb_groups = [
            {'verb': 'play', 'irregular_past': '', 'preposition': 'with', 'particle': 'up', 'objects': 1}
        ]
        config = {
            'error_probability': 0.0,
            'paragraph_size': 1,
            'probability_negative_verb': 0.0,
            'probability_pronoun': 0.0,
            'probability_plural_noun': 0.0
        }
        word_lists = {
            'verb_groups': verb_groups,
            'countable_nouns': self.countable_nouns,
            'uncountable_nouns': {},
            'static_nouns': {}
        }
        json_data = {'config': config, 'word_lists': word_lists}
        answer = self.app.get('/generate', json=json_data).get_json()['display_str']
        self.assertIn('plays', answer)
        self.assertIn('with', answer)
        self.assertIn('up', answer)

    def test_generate_countable_nouns(self):
        countable_nouns = [
            {'noun': 'child', 'irregular_plural': 'children'}
        ]
        config = {
            'error_probability': 0.0,
            'paragraph_size': 1,
            'probability_pronoun': 0.0,
            'probability_plural_noun': 1.0
        }
        word_lists = {
            'verb_groups': self.verb_groups,
            'countable_nouns': countable_nouns,
            'uncountable_nouns': {},
            'static_nouns': {}
        }
        json_data = {'config': config, 'word_lists': word_lists}
        answer = self.app.get('/generate', json=json_data).get_json()['display_str']
        self.assertIn('children', answer)

    def test_generate_uncountable_nouns(self):
        uncountable_nouns = [
            {'noun': 'water', 'definite': True}
        ]
        config = {
            'error_probability': 0.0,
            'paragraph_size': 1,
            'probability_pronoun': 0.0,
        }
        word_lists = {
            'verb_groups': self.verb_groups,
            'uncountable_nouns': uncountable_nouns,
            'countable_nouns': {},
            'static_nouns': {}
        }
        json_data = {'config': config, 'word_lists': word_lists}
        answer = self.app.get('/generate', json=json_data).get_json()['display_str']
        self.assertIn('the water', answer)

    def test_generate_static_nouns(self):
        static_nouns = [
            {'noun': 'Joe', 'is_plural': False}
        ]
        config = {
            'error_probability': 0.0,
            'paragraph_size': 1,
            'probability_pronoun': 0.0,
            'probability_plural_noun': 1.0
        }
        word_lists = {
            'verb_groups': self.verb_groups,
            'static_nouns': static_nouns,
            'countable_nouns': {},
            'uncountable_nouns': {}
        }
        json_data = {'config': config, 'word_lists': word_lists}
        answer = self.app.get('/generate', json=json_data).get_json()['display_str']
        self.assertIn('Joe', answer)

    def test_query_is_correct_true(self):
        paragraph = Paragraph([
            Sentence([
                Noun('dog').indefinite().capitalize(), Verb('play').third_person(), Punctuation.PERIOD
            ])
        ])
        serialized = Serializer.to_json(paragraph)
        submission_str = 'A dog plays.'
        json_data = {'original_paragraph': serialized, 'submission_str': submission_str}

        answer = self.app.get('/query/is_correct', json=json_data).get_json()
        expected = {'is_correct': True}
        self.assertEqual(answer, expected)

    def test_query_is_correct_true_can_accept_noun_number_change(self):
        paragraph = Paragraph([
            Sentence([
                Noun('dog').indefinite().capitalize(), Verb('play').third_person(), Punctuation.PERIOD
            ]),
            Sentence([
                Noun('dog').definite().capitalize(), Verb('eat').third_person(), Punctuation.PERIOD
            ])
        ])
        serialized = Serializer.to_json(paragraph)
        submission_str = 'Dogs play. The dogs eat.'
        json_data = {'original_paragraph': serialized, 'submission_str': submission_str}

        answer = self.app.get('/query/is_correct', json=json_data).get_json()
        expected = {'is_correct': True}
        self.assertEqual(answer, expected)

    def test_query_is_correct_false(self):
        paragraph = Paragraph([
            Sentence([
                Noun('dog').indefinite().capitalize(), Verb('play').third_person(), Punctuation.PERIOD
            ])
        ])
        serialized = Serializer.to_json(paragraph)
        submission_str = 'A dog play.'
        json_data = {'original_paragraph': serialized, 'submission_str': submission_str}

        answer = self.app.get('/query/is_correct', json=json_data).get_json()
        expected = {'is_correct': False}
        self.assertEqual(answer, expected)

    def test_query_count_word_errors(self):
        paragraph = Paragraph([
            Sentence([
                Noun('dog').indefinite().capitalize(), Verb('play').third_person(), Punctuation.PERIOD
            ])
        ])
        serialized = Serializer.to_json(paragraph)
        submission_str = 'The doggie play.'
        json_data = {'original_paragraph': serialized, 'submission_str': submission_str}

        answer = self.app.get('/query/count_word_errors', json=json_data).get_json()
        expected = {'word_errors': 2}
        self.assertEqual(answer, expected)

    def test_query_count_sentence_errors(self):
        paragraph = Paragraph([
            Sentence([
                Noun('dog').indefinite().capitalize(), Verb('play').third_person(), Punctuation.PERIOD
            ])
        ])
        serialized = Serializer.to_json(paragraph)
        submission_str = 'The doggie play.'
        json_data = {'original_paragraph': serialized, 'submission_str': submission_str}

        answer = self.app.get('/query/count_sentence_errors', json=json_data).get_json()
        expected = {'sentence_errors': 1}
        self.assertEqual(answer, expected)

    def test_query_word_hints(self):
        paragraph = Paragraph([
            Sentence([
                Noun('dog').indefinite().capitalize(), Verb('play').third_person(), Punctuation.PERIOD
            ])
        ])
        serialized = Serializer.to_json(paragraph)
        submission_str = 'The doggie play.'
        json_data = {'original_paragraph': serialized, 'submission_str': submission_str}

        answer = self.app.get('/query/word_hints', json=json_data).get_json()
        expected = {
            'word_errors': 2,
            'hint_paragraph': '<bold>The doggie</bold> <bold>play</bold>.',
            'missing_sentences': 0
        }
        self.assertEqual(answer, expected)

    def test_query_sentence_hints(self):
        paragraph = Paragraph([
            Sentence([
                Noun('dog').indefinite().capitalize(), Verb('play').third_person(), Punctuation.PERIOD
            ])
        ])
        serialized = Serializer.to_json(paragraph)
        submission_str = 'The doggie play.'
        json_data = {'original_paragraph': serialized, 'submission_str': submission_str}

        answer = self.app.get('/query/sentence_hints', json=json_data).get_json()
        expected = {
            'sentence_errors': 1,
            'hint_paragraph': '<bold>The doggie play.</bold>',
            'missing_sentences': 0
        }
        self.assertEqual(answer, expected)

    def test_catch_bad_json_str(self):
        json_str = json.dumps({'config': {}, 'word_lists': self.word_lists})
        bad_json = json_str[:-2]
        answer = self.app.get('/generate', data=bad_json, content_type='application/json').get_json()
        expected = {
            'status_code': 400,
            'error_type': 'BadRequest',
            'title': 'Bad Request',
            'text': answer['text']
        }
        self.assertEqual(answer, expected)

    def test_generate_internal_error_due_to_bad_config_as_acts_in_actual_app(self):
        test_app = flask_app.create_app()
        client = test_app.test_client()

        json_data = {'config': {'error_probability': 'banana'}, 'word_lists': self.word_lists}
        answer = client.get('/generate', json=json_data).get_json()
        expected = {'error_type': 'TypeError',
                    'status_code': 500,
                    'text': "'<' not supported between instances of 'float' and 'str'",
                    'title': 'internal server error'}
        self.assertEqual(answer, expected)
