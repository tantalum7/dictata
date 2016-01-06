
# Library imports
import Tkinter as tk
from threading import Thread


class GuiThread(Thread):

    def __init__(self):

        # Call thread initialiser
        Thread.__init__(self)

        # Self start the thread ( run() )
        self.start()

    def _window_quit_handler(self):

        # Close down tkinter if the quit button is pressed
        self.root.quit()

    def run(self):

        # Start Tkinter root
        self.root = tk.Tk()

        # Bind windows close event
        self.root.protocol("WM_DELETE_WINDOW", self._window_quit_handler)

        self.rich_editor = tk.Text(self.root)
        self.rich_editor.pack()

        # Start the main tkinter loop, stay here to the GUI closes
        self.root.mainloop()


if __name__ == "__main__":

    gui = GuiThread()

    while True:
        pass