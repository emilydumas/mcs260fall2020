"""
Letter rotation GUI encoder/decoder application
MCS 260 Fall 2020 Lecture 38 (10am)
"""

import tkinter
import tkinter.ttk
import rotcode

class EncoderApp(tkinter.Tk):
    """Main window of the encoder application"""
    def __init__(self):
        """Initialize the GUI"""
        super().__init__()

        self.input_string = tkinter.StringVar()
        self.input_string.trace_add("write",lambda a,b,c:self.handle_input_text_change() )

        self.output_string = tkinter.StringVar()

        self.input_label = tkinter.ttk.Label(self,text="Input:")
        self.input_label.grid(row=0,column=0,sticky="w")

        self.output_label = tkinter.ttk.Label(self,text="Output:")
        self.output_label.grid(row=1,column=0,sticky="w")

        self.input_entry = tkinter.ttk.Entry(self,textvariable=self.input_string,width=30)
        self.input_entry.grid(row=0,column=1,columnspan=2,sticky="ew")

        self.output_entry = tkinter.ttk.Entry(self,textvariable=self.output_string,width=30)
        self.output_entry.grid(row=1,column=1,columnspan=2,sticky="ew")

        self.steps_label = tkinter.ttk.Label(self,text="Steps:")
        self.steps_label.grid(row=2,column=0,sticky="w")

        self.steps_slider = tkinter.ttk.Scale(self)
        self.steps_slider.grid(row=2,column=1,sticky="ew")

        self.steps_display = tkinter.ttk.Label(self,text="99",width=2)
        self.steps_display.grid(row=2,column=2)

        self.reverse_check = tkinter.ttk.Checkbutton(self,text="Reverse string")
        self.reverse_check.grid(row=3,column=1,sticky="w")

    def handle_input_text_change(self):
        """Callback for changes in the input text entry box"""
        s = self.input_string.get()
        senc = rotcode.rotate(s,steps=13)
        self.output_string.set(senc)

app = EncoderApp()
app.mainloop()
