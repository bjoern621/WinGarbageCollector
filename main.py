from tkinter import *
from tkinter import ttk
from GarbageInfo import *
from ScrollArea import ScrollArea

class MainWindow:
    def __init__(self, root: Tk) -> None:
        # Application window
        root.title("Windows Garbage Collector")

        standard_width = 500
        standard_heigth = 300
        screen_width = root.winfo_screenwidth()
        screen_heigth = root.winfo_screenheight()

        root.minsize(width=standard_width, height=standard_heigth)

        # Application window position
        top_left_x = int(screen_width / 2 - standard_width / 2)
        top_left_y = int(screen_heigth / 2 - standard_heigth / 2)
        root.geometry(f"{standard_width}x{standard_heigth}+{top_left_x}+{top_left_y}")

        # Main frame
        main_frame = ttk.Frame(root).pack()

        # Scroll area
        scroll_area = ScrollArea(main_frame)

        # Buttons
        button_frame = ttk.Frame(main_frame, padding=7.5, style="button_frame.TFrame")

        ttk.Button(button_frame, text="Beenden", command=lambda: root.quit(), style="button_frame.TButton").pack(side=RIGHT, padx=(7.5, 0))
        ttk.Button(button_frame, text="Bestätigen", style="button_frame.TButton").pack(side=RIGHT)

        button_frame.pack(fill=X, side=BOTTOM)
        scroll_area.pack(expand=True, fill=BOTH)

        # Styling
        s = ttk.Style(main_frame)
        s.configure("button_frame.TFrame", background="lightgrey")
        s.configure("button_frame.TButton", background="lightgrey")

if __name__ == "__main__":
    garbage_list = [
        ("Programme deinstallieren", RemoveAppPackageGarbageInfo("Clipchamp", "Clipchamp.Clipchamp", False))
    ]

    root = Tk()
    MainWindow(root)
    root.mainloop()