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
        self.title("Shark Encode Plus Max")

        # String for input text
        self.input_string = tkinter.StringVar()
        self.input_string.trace_add("write",lambda a,b,c:self.recompute_output_text() )

        # String to display in the output box
        self.output_string = tkinter.StringVar()

        self.input_label = tkinter.ttk.Label(self,text="Input:")
        self.input_label.grid(row=0,column=0,sticky="w",padx=6,pady=3)

        self.output_label = tkinter.ttk.Label(self,text="Output:")
        self.output_label.grid(row=1,column=0,sticky="w",padx=6,pady=3)

        self.input_entry = tkinter.ttk.Entry(self,textvariable=self.input_string,width=50)
        self.input_entry.grid(row=0,column=1,columnspan=2,sticky="ew",padx=6,pady=3)

        self.output_entry = tkinter.ttk.Entry(self,textvariable=self.output_string,state="readonly",width=50)
        self.output_entry.grid(row=1,column=1,columnspan=2,sticky="ew",padx=6,pady=3)

        self.steps_label = tkinter.ttk.Label(self,text="Steps:")
        self.steps_label.grid(row=2,column=0,sticky="w",padx=6,pady=3)

        # Integer for number of steps to rotate input string
        self.steps = tkinter.IntVar()
        self.steps.trace_add("write",lambda a,b,c:self.recompute_output_text())
        self.steps.trace_add("write",lambda a,b,c:self.update_steps_display())

        self.steps_slider = tkinter.ttk.Scale(self,from_=0,to=25,variable=self.steps)
        self.steps_slider.grid(row=2,column=1,sticky="ew",padx=6,pady=3)

        self.steps_display = tkinter.ttk.Label(self,text="??",width=2)
        self.steps_display.grid(row=2,column=2,padx=6,pady=3,sticky="w")

        # Integer 0 for no reversal, 1 for reversal
        self.reverse_flag = tkinter.IntVar()
        self.reverse_flag.trace_add("write",lambda a,b,c:self.recompute_output_text())

        self.reverse_check = tkinter.ttk.Checkbutton(self,text="Reverse string",variable=self.reverse_flag)
        self.reverse_check.grid(row=3,column=1,sticky="w")

        self.exit_button = tkinter.ttk.Button(self,text="Exit",command=exit)
        self.exit_button.grid(row=3,column=2,padx=6,pady=3,sticky="e")

        # Initialize the steps display to agree with the value
        # of the slider
        self.update_steps_display()

    def update_steps_display(self):
        """Update numeric display next to the steps slider"""
        self.steps_display["text"] = str(self.steps.get())

    def recompute_output_text(self):
        """Recompute output text from given input, steps, reverse flag"""
        s = self.input_string.get()
        senc = rotcode.rotate(s,steps=self.steps.get())
        if self.reverse_flag.get():
            # Reverse the encoded text
            senc = senc[::-1]
        self.output_string.set(senc)

app = EncoderApp()
app.mainloop()
