

class GenericBackend(object):

    class StorageInitaliseException(Exception):
        pass

    class StorageOpenException(Exception):
        pass

    class ObjectNotFoundException(Exception):
        pass

    def initialise(self, settings):
        pass

    def open(self, path):
        pass

    def close(self):
        pass

    def get_object(self, object_id):
        pass

    def put_object(self, object_id):
        pass

    def synchronise(self):
        pass

