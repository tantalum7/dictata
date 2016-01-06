
# Library imports


# Project imports
from storage    import Storage
from gui        import GuiThread


class Dictata(object):

    def __init__(self):

        self.gui = GuiThread()

        self.storage = Storage()

        self.storage.open("test.json")

        index = self.storage.rebuild_index()

        self.gui.add_job({'redraw_index' : index})

        pass

    def run(self):

        self.gui.start()

        while self.gui.isAlive():
            pass

