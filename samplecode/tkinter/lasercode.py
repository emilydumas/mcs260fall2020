"""
GUI for letter rotation encoding of strings
MCS 260 Fall 2020 Lecture 38 (2pm)
"""
import tkinter
import tkinter.ttk
import rotcode

class EncoderApp(tkinter.Tk):
    """GUI for controlling rotcode.rotate"""
    def __init__(self):
        """Initialize the window and add widgets"""
        super().__init__()  # Actually makes the main window
        self.title("LaserCode 9 Series X+")

        self.input_text = tkinter.StringVar()
        self.input_text.trace_add("write",lambda a,b,c:self.input_text_changed())
        self.output_text = tkinter.StringVar()

        self.input_label = tkinter.ttk.Label(self,text="Input:")
        self.input_label.grid(row=0,column=0,sticky="w")

        self.output_label = tkinter.ttk.Label(self,text="Output:")
        self.output_label.grid(row=1,column=0,sticky="w")

        self.input_entry = tkinter.ttk.Entry(self,width=50,textvariable=self.input_text)
        self.input_entry.grid(row=0,column=1,columnspan=2,sticky="ew")

        self.output_entry = tkinter.ttk.Entry(self,width=50,textvariable=self.output_text)
        self.output_entry.grid(row=1,column=1,columnspan=2,sticky="ew")

        self.steps_label = tkinter.ttk.Label(self,text="Steps:")
        self.steps_label.grid(row=2,column=0,sticky="w")

        self.steps_slider = tkinter.ttk.Scale(self)
        self.steps_slider.grid(row=2,column=1,sticky="ew")

        self.steps_indicator = tkinter.ttk.Label(self,text="99",width=2)
        self.steps_indicator.grid(row=2,column=2,sticky="w")

        self.reverse_check = tkinter.ttk.Checkbutton(self,text="Reverse string")
        self.reverse_check.grid(row=3,column=1,sticky="w")

    def input_text_changed(self):
        """callback for changes to input text entry box"""
        s = self.input_text.get()
        senc = rotcode.rotate(s,13)
        self.output_text.set(senc)

app = EncoderApp()
app.mainloop()
