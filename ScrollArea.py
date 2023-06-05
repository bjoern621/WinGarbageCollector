from tkinter import *
from tkinter import ttk
from typing import Tuple
from ToggleAllCheckbutton import ToggleAllCheckbutton

class ScrollArea(ttk.Frame):
    def __init__(self, master, garbage_list) -> None:
        super().__init__(master)

        s = ttk.Style()
        s.configure("alternate_background.TCheckbutton", background="white")

        content_canvas = Canvas(self, width=0, height=0, highlightthickness=0)
        content_canvas.pack(side=LEFT, expand=True, fill=BOTH)

        scrollbar = ttk.Scrollbar(self, command=content_canvas.yview)
        scrollbar.pack(side=RIGHT, fill=Y)

        # Scroll
        content_canvas.configure(yscrollcommand=scrollbar.set)
        content_canvas.bind("<Configure>", lambda event: self.update_scrollbar_and_frame(content_canvas, content_frame, content_frame_id))
        content_canvas.bind_all("<MouseWheel>", lambda event: content_canvas.yview_scroll(int(-1 * (event.delta / 120)), UNITS))

        content_frame = ttk.Frame(content_canvas)
        #content_frame.bind("<Configure>", lambda event: self._configure_interior(self.content_canvas, self.content_frame))

        content_frame_id = content_canvas.create_window((0, 0), window=content_frame, anchor=NW)

        self.populate_list(content_frame=content_frame, list=garbage_list)
    
    def populate_list(self, content_frame: ttk.Frame, list):
        toggle_all = ToggleAllCheckbutton(master=content_frame, text="Toggle All", takefocus=False)
        toggle_all.pack()

        for number in range(1, 31):
            pair = self.add_checkbox(content_frame=content_frame)

            toggle_all.add_child_checkbox(pair[1])

            if number % 2 == 0:
                pair[0].configure(style="alternate_background.TCheckbutton")

    def add_toggle_all_checkbox(self):
        pass

    def add_checkbox(self, content_frame: ttk.Frame) -> Tuple[ttk.Checkbutton, IntVar]:
        value = IntVar(value=1)
        checkbox = ttk.Checkbutton(content_frame, text="Clipchamp entfernen", takefocus=False, padding=(20, 5, 0, 5), variable=value)
        checkbox.pack(fill=X)

        return (checkbox, value)
    
    def update_scrollbar_and_frame(self, canvas: Canvas, inner_frame: ttk.Frame, inner_frame_id: int):
        canvas.config(scrollregion=canvas.bbox("all"))

        if inner_frame.winfo_width() != canvas.winfo_width():
            # Update the inner frame's width to fill the canvas.
            canvas.itemconfigure(inner_frame_id, width=canvas.winfo_width())
        
    #For updating canvas later (if frame changed, e.g. an option was expanded)
    def _configure_interior(self, canvas: Canvas, inner_frame: ttk.Frame):
        # Update the scrollbar to match the size of the inner frame.   
        return
