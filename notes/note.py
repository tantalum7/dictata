
# Library imports
from time import time
from datetime import datetime


class Note(object):

    def __init__(self, document):

        # Init class vars
        self._document = document

    @property
    def uid(self):
        return self._document.uid

    @property
    def title(self):
        return self._document['title']

    @title.setter
    def title(self, new_title):
        self._document['title'] = new_title
        self._touch()

    @property
    def body(self):
        return self._document['body']

    @body.setter
    def body(self, new_body):
        self._document['body'] = new_body
        self._touch()

    @property
    def tags(self):
        return self._document['tags']

    @tags.setter
    def tags(self, new_tags):
        self._document['tags'] = new_tags
        self._touch()

    @property
    def parent(self):
        return self._document['parent']

    @parent.setter
    def parent(self, new_parent):
        self._document['parent'] = new_parent
        self._touch()

    @property
    def creation_time(self):
        return float(self._document['creation_time'])

    @property
    def creation_date(self):
        return datetime.fromtimestamp(int(self.creation_time)).strftime('%d %b %Y')

    @property
    def last_edit_time(self):
        return float(self._document['last_edit_time'])

    @property
    def last_edit_date(self):
        return datetime.fromtimestamp(int(self.last_edit_time)).strftime('%d %b %Y')

    @property
    def meta(self):
        return self._document['meta']

    @meta.setter
    def meta(self, new_meta):
        self._document['meta'] = new_meta

    def _touch(self):
        self._document["last_edit_time"] = time()
