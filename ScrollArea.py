from tkinter import *
from tkinter import ttk

class ScrollArea(ttk.Frame):
    def __init__(self, master) -> None:
        super().__init__(master)

        s = ttk.Style()
        s.configure("TFrame", background="blue")
        s.configure("TButton", background="red")

        content_canvas = Canvas(self, background="yellow", width=0, height=0)
        content_canvas.pack(side=LEFT, expand=True, fill=BOTH)

        scrollbar = ttk.Scrollbar(self, command=content_canvas.yview)
        scrollbar.pack(side=RIGHT, fill=Y)

        # Scroll
        content_canvas.configure(yscrollcommand=scrollbar.set)
        content_canvas.bind("<Configure>", lambda event: content_canvas.configure(scrollregion=content_canvas.bbox("all")))
        content_canvas.bind_all("<MouseWheel>", lambda event: content_canvas.yview_scroll(int(-1 * (event.delta / 120)), UNITS))

        content_frame = ttk.Frame(content_canvas)

        content_canvas.create_window((0, 0), window=content_frame, anchor=NW, width=150)

        for number in range(1, 41):
            ttk.Button(content_frame, text=f"This is {number}, Yeah!").pack()



