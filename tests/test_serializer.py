import pickle
import unittest

from paragraph_generator import Paragraph, Sentence, BasicWord, Verb, Pronoun, Punctuation, BeVerb
from paragraph_generator.tags.status_tag import StatusTag
from paragraph_generator.tags.tags import Tags
from paragraph_generator.words.noun import Noun

from paragraph_generator_flask.serializer import Serializer


class TestSerializer(unittest.TestCase):
    def test_serialize_empty_paragraph(self):
        to_send = Paragraph([])
        serialized = Serializer.serialize(to_send)
        expected = pickle.dumps(to_send)
        self.assertEqual(serialized, expected)

    def test_de_serialize_empty_paragraph(self):
        to_send = Paragraph([])
        serialized = Serializer.serialize(to_send)
        de_serialized = Serializer.de_serialize(serialized)
        self.assertEqual(de_serialized, to_send)

    def test_serialize_actual_paragraph(self):
        to_send = Paragraph([
            Sentence([
                BasicWord('a'), Verb('a'), Noun('a'), Pronoun.I, Punctuation.COMMA, BeVerb.AM
            ])
        ], Tags([StatusTag.RAW]))
        serialized = Serializer.serialize(to_send)
        expected = pickle.dumps(to_send)
        self.assertEqual(serialized, expected)

    def test_de_serialize_actual_paragraph(self):
        to_send = Paragraph([
            Sentence([
                BasicWord('a'), Verb('a'), Noun('a'), Pronoun.I, Punctuation.COMMA, BeVerb.AM
            ])
        ], Tags([StatusTag.RAW]))
        serialized = Serializer.serialize(to_send)
        print(serialized)
        de_serialized = Serializer.de_serialize(serialized)
        self.assertEqual(de_serialized, to_send)


