from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog, messagebox
from tkinter.scrolledtext import ScrolledText
from func_clean import garbagefile_clean_mode1, garbagefile_clean_mode2
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)  # solve the problem of blur effect in windows


CHOSE1 = None
CHOSE2 = None


def callback1():
    global CHOSE1, text1
    CHOSE1 = filedialog.askdirectory()
    text1.insert(END, f'chosen {CHOSE1}\n')
    text1.update_idletasks()


def callback2():
    global CHOSE2, text2
    CHOSE2 = filedialog.askdirectory()
    text2.insert(END, f'chosen {CHOSE2}\n')
    text2.update_idletasks()


def dump1():
    global CHOSE1, text1, spin1
    N = int(spin1.get()) if spin1.get() != '' else 0
    res = garbagefile_clean_mode1(CHOSE1, N)
    if len(res) == 0:
        text1.insert(END, 'deleted nothing\n')
        text1.update_idletasks()
    else:
        for s in res:
            text1.insert(END, f'deleted {s} success\n')
            text1.update_idletasks()


def dump2():
    global CHOSE2, text2, spin2
    N = int(spin2.get()) if spin2.get() != '' else 0
    res = garbagefile_clean_mode2(CHOSE2, N)
    if len(res) == 0:
        text2.insert(END, 'deleted nothing\n')
        text2.update_idletasks()
    else:
        for s in res:
            text2.insert(END, f'deleted {s} success\n')
            text2.update_idletasks()



root = Tk()
root.geometry("1500x600+400+300")
root.title("funny tool of cleaning garbage file")
root.resizable(0, 0)
notebook = Notebook(root)
frame1 = Frame()
frame2 = Frame()
frame3 = Frame()
notebook.add(frame1, text="mode1: clean older")
notebook.add(frame2, text="mode2: clean smaller")
notebook.add(frame3, text="help file")
notebook.pack(padx=10, pady=10, fill=BOTH, expand=TRUE)

file_config = Button(frame1, text="chose the folder", command=callback1)
spin1 = Spinbox(frame1, from_=0, to=100000, increment=1)
label = Label(frame1, text="expire days:")
dump_config = Button(frame1, text="dump it!", command=dump1)

text1 = ScrolledText(frame1, height=18, width=50)
text1.insert(END, "logging here: \n\n")
text1.place(x=0, y=20)
file_config.place(x=760, y=20)
label.place(x=760, y=100)
spin1.place(x=960, y=100)
dump_config.place(x=760, y=180)

file_config2 = Button(frame2, text="chose the folder", command=callback2)
spin2 = Spinbox(frame2, from_=0, to=100000, increment=1)
label2 = Label(frame2, text="garbage size:")
dump_config2 = Button(frame2, text="dump it!", command=dump2)

text2 = ScrolledText(frame2, height=18, width=50)
text2.insert(0.0, "logging here: \n\n")
text2.place(x=0, y=20)
file_config2.place(x=760, y=20)
label2.place(x=760, y=100)
spin2.place(x=960, y=100)
dump_config2.place(x=760, y=180)


text3 = ScrolledText(frame3, height=17, width=100)
text3.pack(pady=20)
text3.insert(END, "usage:\n\n")

text3.insert(END, "mode1: clean old garbage files you want\n\n")
text3.insert(END, "mode2: clean the disgusting smaller garbage files\n")

mainloop()
