import Tkinter
import tkFont


"""
Store formatting somehow, either embedded tags (xml or markdown) or a chunk at the end.
 - Would be better to store the formatting in a standard-ish format for backward compatability. Maybe html?

1. Load file, strip out formatting and parse as plain text, insert into textbox.
2. Iterate through all formatting, and add tags to the text to apply the formatting required.

Allow simple formatting, akin to rich text. Something like markdown (bold, italic, heading styles, lists etc).


"""

root = Tkinter.Tk()

default_font = tkFont.Font(root=root, family='Arial', size=10, weight="normal")
bold_font    = tkFont.Font(family='Arial', size=10, weight="bold")

editor = Tkinter.Text()
editor.pack(fill=Tkinter.Y, expand=1)

editor.config(font=default_font)

editor.focus_set()

editor.insert("1.0", "Some very important text here")




editor.tag_config('bold', {'font' : bold_font})
editor.tag_add("bold", "1.5", "1.10")
editor.tag_add("bold", "1.20", "end")

ranges = editor.tag_ranges("sel")

print ranges[0].string

print tkFont.families()
Tkinter.mainloop()