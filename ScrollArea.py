from tkinter import *
from tkinter import ttk

class ScrollArea(ttk.Frame):
    def __init__(self, master) -> None:
        super().__init__(master)

        content_canvas = Canvas(self)
        content_canvas.pack(side=LEFT, fill=BOTH)

        scrollbar = ttk.Scrollbar(self, command=content_canvas.yview)
        scrollbar.pack(side=RIGHT, fill=Y)

        content_canvas.configure(yscrollcommand=scrollbar.set)
        content_canvas.bind("<Configure>", lambda event: content_canvas.configure(scrollregion=content_canvas.bbox("all")))

        content_frame = ttk.Frame(content_canvas)

        content_canvas.create_window((0, 0), window=content_frame, anchor=NW)

        button = ttk.Button(content_frame, text="aoiwdjoiadjowa").pack()
        button = ttk.Button(content_frame, text="aoiwdjoiadjowa").pack()
        button = ttk.Button(content_frame, text="aoiwdjoiadjowa").pack()
        button = ttk.Button(content_frame, text="aoiwdjoiadjowa").pack()
        button = ttk.Button(content_frame, text="aoiwdjoiadjowa").pack()
        button = ttk.Button(content_frame, text="aoiwdjoiadjowa").pack()
        button = ttk.Button(content_frame, text="aoiwdjoiadjowa").pack()
        button = ttk.Button(content_frame, text="aoiwdjoiadjowa").pack()
        button = ttk.Button(content_frame, text="aoiwdjoiadjowa").pack()
        button = ttk.Button(content_frame, text="aoiwdjoiadjowa").pack()
        button = ttk.Button(content_frame, text="aoiwdjoiadjowa").pack()
        button = ttk.Button(content_frame, text="aoiwdjoiadjowa").pack()
        button = ttk.Button(content_frame, text="aoiwdjoiadjowa").pack()
        button = ttk.Button(content_frame, text="aoiwdjoiadjowa").pack()
        button = ttk.Button(content_frame, text="aoiwdjoiadjowa").pack()
        button = ttk.Button(content_frame, text="aoiwdjoiadjowa").pack()
        button = ttk.Button(content_frame, text="aoiwdjoiadjowa").pack()
        button = ttk.Button(content_frame, text="aoiwdjoiadjowa").pack()
        button = ttk.Button(content_frame, text="aoiwdjoiadjowa").pack()
        button = ttk.Button(content_frame, text="aoiwdjoiadjowa").pack()
        button = ttk.Button(content_frame, text="aoiwdjoiadjowa").pack()
        button = ttk.Button(content_frame, text="aoiwdjoiadjowa").pack()
        button = ttk.Button(content_frame, text="aoiwdjoiadjowa").pack()
        button = ttk.Button(content_frame, text="aoiwdjoiadjowa").pack()
        button = ttk.Button(content_frame, text="aoiwdjoiadjowa").pack()
        button = ttk.Button(content_frame, text="aoiwdjoiadjowa").pack()
        button = ttk.Button(content_frame, text="aoiwdjoiadjowa").pack()
        button = ttk.Button(content_frame, text="aoiwdjoiadjowa").pack()
        button = ttk.Button(content_frame, text="aoiwdjoiadjowa").pack()
        button = ttk.Button(content_frame, text="aoiwdjoiadjowa").pack()
        button = ttk.Button(content_frame, text="aoiwdjoiadjowa").pack()
        button = ttk.Button(content_frame, text="aoiwdjoiadjowa").pack()
        button = ttk.Button(content_frame, text="aoiwdjoiadjowa").pack()
        button = ttk.Button(content_frame, text="aoiwdjoiadjowa").pack()
        button = ttk.Button(content_frame, text="aoiwdjoiadjowa").pack()
        button = ttk.Button(content_frame, text="aoiwdjoiadjowa").pack()
        button = ttk.Button(content_frame, text="aoiwdjoiadjowa").pack()
        button = ttk.Button(content_frame, text="aoiwdjoiadjowa").pack()
        button = ttk.Button(content_frame, text="aoiwdjoiadjowa").pack()
        button = ttk.Button(content_frame, text="aoiwdjoiadjowa").pack()
        button = ttk.Button(content_frame, text="aoiwdjoiadjowa").pack()
        button = ttk.Button(content_frame, text="aoiwdjoiadjowa").pack()
        button = ttk.Button(content_frame, text="aoiwdjoiadjowa").pack()
        button = ttk.Button(content_frame, text="aoiwdjoiadjowa").pack()
        button = ttk.Button(content_frame, text="aoiwdjoiadjowa").pack()
        button = ttk.Button(content_frame, text="aoiwdjoiadjowa").pack()
        button = ttk.Button(content_frame, text="aoiwdjoiadjowa").pack()
        button = ttk.Button(content_frame, text="aoiwdjoiadjowa").pack()
        button = ttk.Button(content_frame, text="aoiwdjoiadjowa").pack()
        button = ttk.Button(content_frame, text="aoiwdjoiadjowa").pack()
        button = ttk.Button(content_frame, text="aoiwdjoiadjowa").pack()
        button = ttk.Button(content_frame, text="aoiwdjoiadjowa").pack()
        button = ttk.Button(content_frame, text="aoiwdjoiadjowa").pack()
        button = ttk.Button(content_frame, text="aoiwdjoiadjowa").pack()
        button = ttk.Button(content_frame, text="aoiwdjoiadjowa").pack()
        button = ttk.Button(content_frame, text="aoiwdjoiadjowa").pack()
        button = ttk.Button(content_frame, text="aoiwdjoiadjowa").pack()
        button = ttk.Button(content_frame, text="aoiwdjoiadjowa").pack()
        button = ttk.Button(content_frame, text="aoiwdjoiadjowa").pack()
        button = ttk.Button(content_frame, text="aoiwdjoiadjowa").pack()
        button = ttk.Button(content_frame, text="aoiwdjoiadjowa").pack()
        button = ttk.Button(content_frame, text="aoiwdjoiadjowa").pack()
        button = ttk.Button(content_frame, text="aoiwdjoiadjowa").pack()
        button = ttk.Button(content_frame, text="aoiwdjoiadjowa").pack()

