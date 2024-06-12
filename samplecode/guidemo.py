"""
GUI demonstration using tkinter
MCS 260 Fall 2020 Lecture 36 - Emily Dumas
"""

import tkinter
import tkinter.ttk

app = tkinter.Tk()

# Create a Label widget
lbl = tkinter.ttk.Label(app,text="",width=35,anchor="center")
# Place the widget using grid layout manager
lbl.grid(row=0,column=0,padx=5,pady=5)

# Functions that handle button presses
def show_message():
    """Display an inspiring message"""
    lbl["text"] = "Your project 4 idea is great!"

def hide_message():
    """Clear the Label widget"""
    lbl["text"] = ""

# Add the buttons
# (note: it's ok that we overwrite the value of btn
#  several times, as long as we're done calling its
#  methods.)
btn = tkinter.ttk.Button(app,text="Show message",command=show_message)
btn.grid(row=1,column=0,padx=5,pady=2,sticky="ew")
btn = tkinter.ttk.Button(app,text="Clear message",command=hide_message)
btn.grid(row=2,column=0,padx=5,pady=2,sticky="ew")
btn = tkinter.ttk.Button(app,text="Quit",command=exit)
btn.grid(row=3,column=0,padx=5,pady=2,sticky="ew")

# Checkbox demo --- it doesn't do anything right now!
checkbox = tkinter.ttk.Checkbutton(app,text="Verify project 4 proposal")
checkbox.grid(row=4,column=0,padx=5,pady=2,sticky="ew")

# Slider demo --- it doesn't do anything right now!
slider = tkinter.ttk.Scale(app)
slider.grid(row=5,column=0,padx=5,pady=2,sticky="ew")

# Text entry box demo --- it doesn't do anything right now!
entry = tkinter.ttk.Entry(app)
entry.grid(row=6,column=0,padx=5,pady=2,sticky="ew")

app.mainloop()
