import tkinter as tk

class App:
    
    def __init__(self, master):
        frame = tk.Frame(master)
        frame.pack()
        self.button = tk.Button(frame, text="QUIT", fg="red", command=frame.quit)
        self.button.pack(side=tk.LEFT)
        self.hi_there = tk.Button(frame, text="sapaan", command=self.ucapan)
        self.hi_there.pack(side=tk.LEFT)

    def ucapan(self):
        print ("Hallo semua!")

root = tk.Tk()
root.title("GUI Sapaan sederhana")
app = App(root)
root.mainloop()

