"""
GUI for letter rotation encoding of strings
With slow encoding in a worker thread so the GUI
remains responsive.
MCS 260 Fall 2020 Lecture 43 (2pm)
"""
import tkinter
import tkinter.ttk
import rotcode
import time
import threading

class EncoderModel:
    """Model for the encoder application"""
    def __init__(self):
        """Create tkinter variables and attach recalculate callback"""
        self.output_text = tkinter.StringVar()

        self.input_text = tkinter.StringVar()
        self.input_text.trace_add("write",lambda a,b,c:self.recalculate())

        self.steps = tkinter.IntVar()
        self.steps.trace_add("write",lambda a,b,c:self.recalculate())

        self.reverse_flag = tkinter.IntVar()
        self.reverse_flag.trace_add("write",lambda a,b,c:self.recalculate())

        self.recalculation_needed = threading.Event()

        self.worker = threading.Thread(target=self.worker_main,daemon=True)
        self.worker.start()

    def worker_main(self):
        """Main function of the worker thread that handles encoding"""
        while True:
            self.recalculation_needed.wait()
            self.recalculation_needed.clear()
            s = self.input_text.get()
            senc = rotcode.rotate(s,self.steps.get())
            time.sleep(1)
            if self.reverse_flag.get():
                # Reverse the encoded string
                senc = senc[::-1]
            # Show the result, but only if it is up to date
            if not self.recalculation_needed.is_set():
                self.output_text.set(senc)

    def recalculate(self):
        """Recalculate output_text from the values of input_text,
        steps, and reverse_flag"""
        self.output_text.set("[WORK IN PROGRESS]")
        # Set recalculation_needed boolean to True
        # signaling the worker thread to wake up and do work
        self.recalculation_needed.set()

class EncoderApp(tkinter.Tk):
    """GUI for controlling rotcode.rotate"""
    def __init__(self):
        """Initialize the window and add widgets"""
        super().__init__()  # Actually makes the main window
        self.title("LaserCode 9 Series X+")

        self.model = EncoderModel()
        
        self.input_label = tkinter.ttk.Label(self,text="Input:")
        self.input_label.grid(row=0,column=0,sticky="w",padx=8,pady=4)

        self.output_label = tkinter.ttk.Label(self,text="Output:")
        self.output_label.grid(row=1,column=0,sticky="w",padx=8,pady=4)

        self.input_entry = tkinter.ttk.Entry(self,width=50,textvariable=self.model.input_text)
        self.input_entry.grid(row=0,column=1,columnspan=2,sticky="ew",padx=8,pady=4)

        self.output_entry = tkinter.ttk.Entry(self,width=50,state="readonly",textvariable=self.model.output_text)
        self.output_entry.grid(row=1,column=1,columnspan=2,sticky="ew",padx=8,pady=4)

        self.steps_label = tkinter.ttk.Label(self,text="Steps:")
        self.steps_label.grid(row=2,column=0,sticky="w",padx=8,pady=4)

        self.model.steps.trace_add("write",lambda a,b,c:self.update_steps_indicator())

        self.steps_slider = tkinter.ttk.Scale(self,from_=0,to=25,variable=self.model.steps)
        self.steps_slider.grid(row=2,column=1,sticky="ew",padx=8,pady=4)

        self.steps_indicator_content = tkinter.StringVar()

        self.steps_indicator = tkinter.ttk.Label(self,textvariable=self.steps_indicator_content,width=2)
        self.steps_indicator.grid(row=2,column=2,sticky="w",padx=8,pady=4)

        self.reverse_check = tkinter.ttk.Checkbutton(self,text="Reverse string",variable=self.model.reverse_flag)
        self.reverse_check.grid(row=3,column=1,sticky="w",padx=8,pady=4)

        self.exit_button = tkinter.ttk.Button(self,text="Exit",command=exit)
        self.exit_button.grid(row=3,column=2,sticky="e",padx=8,pady=4)

        # Initialize the steps indicator to whatever the initial
        # value of the step slider is.
        self.update_steps_indicator()

    def update_steps_indicator(self):
        """Make steps indicator label consistent with the slider position"""
        self.steps_indicator_content.set(str(self.model.steps.get()))

app = EncoderApp()
app.mainloop()
