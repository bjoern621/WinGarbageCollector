from tkinter import *
from tkinter import ttk

class ScrollArea(ttk.Frame):
    def __init__(self, master) -> None:
        super().__init__(master)

        content_canvas = Canvas(self, width=0, height=0, highlightthickness=0)
        content_canvas.pack(side=LEFT, expand=True, fill=BOTH)

        scrollbar = ttk.Scrollbar(self, command=content_canvas.yview)
        scrollbar.pack(side=RIGHT, fill=Y)

        # Scroll
        content_canvas.configure(yscrollcommand=scrollbar.set)
        content_canvas.bind("<Configure>", lambda event: self.update_scrollbar_and_frame(content_canvas, content_frame, frame_id))
        content_canvas.bind_all("<MouseWheel>", lambda event: content_canvas.yview_scroll(int(-1 * (event.delta / 120)), UNITS))

        content_frame = ttk.Frame(content_canvas)
        #content_frame.bind("<Configure>", lambda event: self._configure_interior(self.content_canvas, self.content_frame))

        frame_id = content_canvas.create_window((0, 0), window=content_frame, anchor=NW)

        for number in range(1, 31):
            ttk.Button(content_frame, text=f"This is {number}, Yeah!").pack()
    
    def update_scrollbar_and_frame(self, canvas: Canvas, inner_frame: ttk.Frame, frame_id: int):
        canvas.config(scrollregion=canvas.bbox("all"))

        if inner_frame.winfo_width() != canvas.winfo_width():
            # Update the inner frame's width to fill the canvas.
            canvas.itemconfigure(frame_id, width=canvas.winfo_width())
        
    #For updating canvas later (if frame changed, e.g. an option was expanded)
    def _configure_interior(self, canvas: Canvas, inner_frame: ttk.Frame):
        # Update the scrollbar to match the size of the inner frame.   
        return
