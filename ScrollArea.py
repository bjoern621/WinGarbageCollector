from tkinter import *
from tkinter import ttk
from typing import Tuple
from ToggleAllCheckbutton import ToggleAllCheckbutton
from GarbageInfo import GarbageInfo

class ScrollArea(ttk.Frame):
    def __init__(self, master, garbage_list: list[GarbageInfo]) -> None:
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

        self.populate_list(content_frame=content_frame, garbage_list=garbage_list)
    
    def populate_list(self, content_frame: ttk.Frame, garbage_list: list[GarbageInfo]):
        last_parent_checkbox_name: str = None
        index = 0

        for garbage_info in garbage_list:
            if garbage_info.parent_checkbox_name != last_parent_checkbox_name:
                last_parent_checkbox_name = garbage_info.parent_checkbox_name

                if garbage_info.parent_checkbox_name != None:
                    # Add new ToggleAllCheckbutton
                    toggle_all_checkbutton: ToggleAllCheckbutton = self.add_toggle_all_checkbox(content_frame, garbage_info.parent_checkbox_name)

                    if index % 2 == 0:
                        toggle_all_checkbutton.configure(style="alternate_background.TCheckbutton")

                    index += 1
                else:
                    # Reset ToggleAllCheckbutton
                    toggle_all_checkbutton = None

            checkbutton_is_child = toggle_all_checkbutton is not None
            checkbutton_variable = IntVar(value=1)

            if checkbutton_is_child:
                toggle_all_checkbutton.add_child_checkbox(checkbutton_variable)

            # Add new Checkbutton
            checkbutton = self.add_checkbox(content_frame=content_frame, text=garbage_info.name, variable=checkbutton_variable, is_child=checkbutton_is_child)

            garbage_info.checkbutton_variable = checkbutton_variable

            if index % 2 == 0:
                checkbutton.configure(style="alternate_background.TCheckbutton")

            index += 1

    def add_toggle_all_checkbox(self, content_frame: ttk.Frame, text:str):
        variable = IntVar(value=1)
        checkbutton = ToggleAllCheckbutton(master=content_frame, text=text, takefocus=False, padding=(20, 5, 0, 5), variable=variable)
        checkbutton.pack(fill=X)

        return checkbutton

    def add_checkbox(self, content_frame: ttk.Frame, text:str, variable: Variable, is_child: bool) -> ttk.Checkbutton:
        if is_child:
            checkbutton = ttk.Checkbutton(content_frame, text=text, takefocus=False, padding=(35, 5, 0, 5), variable=variable)
        else:
            checkbutton = ttk.Checkbutton(content_frame, text=text, takefocus=False, padding=(20, 5, 0, 5), variable=variable)

        checkbutton.pack(fill=X)

        return checkbutton
    
    def update_scrollbar_and_frame(self, canvas: Canvas, inner_frame: ttk.Frame, inner_frame_id: int):
        canvas.config(scrollregion=canvas.bbox("all"))

        if inner_frame.winfo_width() != canvas.winfo_width():
            # Update the inner frame's width to fill the canvas.
            canvas.itemconfigure(inner_frame_id, width=canvas.winfo_width())
        
    #For updating canvas later (if frame changed, e.g. an option was expanded)
    def _configure_interior(self, canvas: Canvas, inner_frame: ttk.Frame):
        # Update the scrollbar to match the size of the inner frame.   
        return
