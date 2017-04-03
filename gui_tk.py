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

        self.master_frame = tk.Frame(self.root, width=500, height=500)

        self.text_editor = TextEditor(self.master_frame, self.root)

        self.master_frame.pack()


    def run(self):
        self.root.mainloop()


class ToolbarButton(tk.Button):

    def __init__(self, master, text, bg=None, **kwargs):

        # Call ancestor init
        tk.Button.__init__(self, master, text=text, bg=bg)

        # Store root and master reference
        self.master = master

        # Create empty nop function
        nop = lambda *args, **kwargs: None

        # Init callback functions
        self.on_click           = kwargs.get('on_click', nop)
        self.on_right_click     = kwargs.get('on_right_click', nop)
        self.on_mouse_enter     = kwargs.get('on_mouse_enter', nop)
        self.on_mouse_leave     = kwargs.get('on_mouse_leave', nop)

        # Bind callback functions
        self.bind("<ButtonRelease-1>", self.on_click)
        self.bind("<ButtonRelease-3>", self.on_right_click)
        self.bind("<Enter>", self.on_mouse_enter)
        self.bind("<Leave>", self.on_mouse_leave)


class TextEditor(tk.Frame):

    def __init__(self, master, root):

        # Call ancestor init
        tk.Frame.__init__(self, master, bg="blue")

        # Store root and master reference
        self.master = master
        self.root = root

        # Create toolbar, and toolbar buttons
        self.toolbar = tk.Frame(self, bg="red")
        self.toolbar_buttons = {'bold'      : ToolbarButton(self.toolbar, text="b", on_click=self.bold_handler),
                                'italic'    : ToolbarButton(self.toolbar, text="i", on_click=self.italic_handler),
                                'underline' : ToolbarButton(self.toolbar, text="u", on_click=self.underline_handler)
        }

        # Pack toolbar and toolbar buttons
        list(map( lambda btn: btn.pack(side=tk.LEFT), self.toolbar_buttons.values() ))
        self.toolbar.pack(side=tk.TOP, fill=tk.X)

        # Create and pack text area
        self.editor = tk.Text(self)
        self.editor.pack(side=tk.TOP, fill=tk.X)

        # Final pack of everything in the frame
        self.pack(side=tk.TOP, fill=tk.X)

        # Prepare fonts
        self.fonts = {}
        self.fonts['default']   = font.Font(root=self.root, family='Arial', size=10)
        self.fonts['bold']      = font.Font(root=self.root, family='Arial', size=10, weight="bold")
        self.fonts['italic']    = font.Font(root=self.root, family='Arial', size=10, slant="italic")
        self.editor.config( {'font' : self.fonts['default']} )

        # Prepare editor tags
        self.editor.tag_config( 'bold', {'font': self.fonts['bold']} )
        self.editor.tag_config( 'italic', {'font': self.fonts['italic']})
        self.editor.tag_config( 'underline', {'underline' : tk.YES} )

        self.editor.tag_raise('bold', 'italic')


    def bold_handler(self, event):
        selection = self.get_text_selection()
        if selection:
            if self.editor.tag_nextrange('bold', selection[0], selection[1]):
                self.editor.tag_remove('bold', selection[0], selection[1])
            else:
                self.editor.tag_add('bold', selection[0], selection[1])

        print("Be bold")

    def italic_handler(self, event):
        selection = self.get_text_selection()
        if selection:
            if self.editor.tag_nextrange('italic', selection[0], selection[1]):
                self.editor.tag_remove('italic', selection[0], selection[1])
            else:
                self.editor.tag_add('italic', selection[0], selection[1])

    def underline_handler(self, event):
        selection = self.get_text_selection()
        if selection:
            if self.editor.tag_nextrange('underline', selection[0], selection[1]):
                self.editor.tag_remove('underline', selection[0], selection[1])
            else:
                self.editor.tag_add('underline', selection[0], selection[1])

    def get_text_selection(self):

        # Grab the start and end range of selection
        start_end = self.editor.tag_ranges("sel")

        # Check we got a tuple for the range
        if start_end:

            # Extract start and end from the tuple
            start, end = start_end

            # Return the selection range - if start and end is the same, return None
            return (start.string, end.string) if start.string != end.string else None

        # We didn't get a range (nothing selected), return none
        else:
            return None





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