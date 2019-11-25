from tkinter import *

if __name__ == "__main__":
    master = Tk()
    master.minsize(450,300)

    Label(master, text="Query").pack()
    Entry(master,width=70).pack()

    master.mainloop()