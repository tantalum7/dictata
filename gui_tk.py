import tkinter as tk
from tkinter import font



"""
Store formatting somehow, either embedded tags (xml or markdown) or a chunk at the end.
 - Would be better to store the formatting in a standard-ish format for backward compatability. Maybe html?

1. Load file, strip out formatting and parse as plain text, insert into textbox.
2. Iterate through all formatting, and add tags to the text to apply the formatting required.

Allow simple formatting, akin to rich text. Something like markdown (bold, italic, heading styles, lists etc).


"""

class ApplicationCore(object):

    def __init__(self):

        self.root = tk.Tk()

        """
        frame:master
            frame:left-sidebar
            frame:editor-container
                frame:editor-toolbar
                    Buttons
                text:editor
        
        """

        self.frames = {}
        self.frames['master'] = tk.Frame(self.root, width=500, height=500)

        self.toolbar = GuiToolbar( self.frames['master'], "toolbar" )

        self.frames['master'].pack(side=tk.TOP)




    def run(self):
        self.root.mainloop()


class GuiToolbar(tk.Frame):

    def __init__(self, master, name, *args, **kwargs):

        # Call ancestor init
        tk.Frame.__init__(self, master, *args, **kwargs)

        # Init class vars
        self.master = master

        self.photo = tk.PhotoImage(file="icons/bold-3x.gif")

        # Init buttons
        self.buttons = []
        self.buttons.append( ToolbarButton(self, text="one", image=self.photo) )
        self.buttons.append( ToolbarButton(self, text="two") )
        self.buttons.append( ToolbarButton(self, text="three") )
        self.pack_all_buttons()

        self.pack()




    def pack_all_buttons(self):
        for button in self.buttons:
            button.pack()



class ToolbarButton(tk.Button):

    def __init__(self, master, *args, **kwargs):

        # Call ancestor init
        tk.Button.__init__(self, master, *args, **kwargs)


"""
root = tk.Tk()

default_font = font.Font(root=root, family='Arial', size=10, weight="normal")
bold_font    = font.Font(family='Arial', size=10, weight="bold")

editor = tk.Text()
editor.pack(fill=tk.Y, expand=1)
editor.config(font=default_font)

editor.focus_set()

editor.insert("1.0", "Some very important text here")




editor.tag_config('bold', {'font' : bold_font})
editor.tag_add("bold", "1.5", "1.10")
editor.tag_add("bold", "1.20", "end")

ranges = editor.tag_ranges("sel")

#print(ranges[0].string)

print( font.families() )
tk.mainloop()
"""

if __name__ == "__main__":


    gui = ApplicationCore()

    gui.run()

    print("Done")