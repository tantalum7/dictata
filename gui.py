
# Library imports
import Tkinter as tk
import ttk
from threading  import Thread
from Queue      import Queue, Empty

import sys

class GuiThread(Thread):

    def __init__(self):

        # Call thread initialiser
        Thread.__init__(self)

        # Init class vars
        self.job_queue  = Queue()
        self.job_table  = {'redraw_index' : self.redraw_index}

    def _window_quit_handler(self):

        # Close down tkinter if the quit button is pressed
        self.root.quit()

    def _create_button_handler(self):

        print "Button pressed"

        self.add_job({'redraw_index' : 'job_stuff'})

    def add_job(self, job_dict):
        self.job_queue.put(job_dict)

    def redraw_index(self, data):
        print "Redrawing index", data
        self.note_tree.delete(*self.note_tree.get_children())

        for uid, title in data[0].items():
            self.note_tree.insert("", 1000, iid=uid, text=title)


    def process_jobs(self):

        try:
            job = self.job_queue.get_nowait()

        # Catch and silently ignore queue empty exceptions
        except Empty:
            pass

        # Raise any other exceptions further up
        except:
            raise

        else:
            print job

            command, data = job.items()[0]

            if command in self.job_table.keys():
                self.job_table[command](data)


        # Ensure this func is called again
        self.root.after(10, self.process_jobs)

    def run(self):

        # Start Tkinter root
        self.root = tk.Tk()

        style = ttk.Style()
        style.configure("TButton", padding=6, relief="flat", foreground="white", background="#2A289D", font=('Ubuntu', 10, 'bold') )
        style.map('TButton', background=[('active', "#4E4CB2")] )


        # Bind windows close event
        self.root.protocol("WM_DELETE_WINDOW", self._window_quit_handler)


        self.create_button = ttk.Button(text="Create Note", command=self._create_button_handler)
        self.create_button.grid(row=0, column=0, sticky="NSWE")

        self.note_tree = ttk.Treeview(self.root)

        self.note_tree.grid(row=1, column=0, sticky="NS")

        self.title_editor = ttk.Entry(self.root)
        self.title_editor.grid(row=0, column=1, sticky="NEWS")

        self.body_editor = tk.Text(self.root)
        self.body_editor.grid(row=1, column=1, rowspan=3)

        # Add our process jobs call into the Tk main event loop
        self.root.after(10, self.process_jobs)

        # Start the main tkinter loop, stay here to the GUI closes
        self.root.mainloop()

        print "Gui loop ends"


if __name__ == "__main__":

    gui = GuiThread()

