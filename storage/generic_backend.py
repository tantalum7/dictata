

class GenericBackend(object):

    def initialise(self, settings):
        raise NotImplemented

    def open(self, path):
        raise NotImplemented

    def close(self, options=None):
        raise NotImplemented

    def get(self, uid, key):
        raise NotImplemented

    def get_document(self, uid):
        raise NotImplemented

    def put(self, uid, key, value):
        raise NotImplemented

    def delete(self, uid, key):
        raise NotImplemented

    def delete_document(self, uid):
        raise NotImplemented

    def sync(self):
        raise NotImplemented

    def count(self, uid):
        raise NotImplemented