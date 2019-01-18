import pickle


class Serializer(object):
    @staticmethod
    def serialize(paragraph):
        return pickle.dumps(paragraph)

    @staticmethod
    def de_serialize(serialized):
        return pickle.loads(serialized)



