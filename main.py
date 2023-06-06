import ctypes
import os
import sys
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from GarbageInfo import *
from ScrollArea import ScrollArea
from fixes.ShowFileExtensions import ShowFileExtensions
from fixes.ShowHiddenFiles import ShowHiddenFiles
from fixes.ClearAutostart import ClearAutostart

class MainWindow:
    def __init__(self, root: Tk) -> None:
        # Application window
        if self.is_admin():
            root.title("Windows Garbage Collector (Administrator)")
        else:
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

        # Loading icon needs time, window size should be set before
        #root.iconbitmap(self.resource_path("images/bin.ico"))

        # Main frame
        main_frame = ttk.Frame(root).pack()

        # Scroll area
        ScrollArea(main_frame, garbage_list).pack(expand=True, fill=BOTH)

        # Button area
        button_frame = ttk.Frame(main_frame, style="button_frame.TFrame", padding=(0, 7.5, 15, 7.5))

        ttk.Button(button_frame, text="Beenden", command=lambda: root.quit(), style="button_frame.TButton", takefocus=False).pack(side=RIGHT, padx=(7.5, 0))
        ttk.Button(button_frame, text="Bestätigen", command=self.run_garbage_collector, style="button_frame.TButton", takefocus=False).pack(side=RIGHT)

        button_frame.pack(fill=X)

        # Styling
        s = ttk.Style(main_frame)
        s.configure("button_frame.TFrame", background="lightgrey")
        s.configure("button_frame.TButton", background="lightgrey")

    def run_garbage_collector(self):
        response = messagebox.askokcancel("Bist du sicher?", 
                                          "Das Programm nimmt unumkehrbare Änderungen vor.\n"
                                          "Bist du sicher, dass du fortfahren möchtest?")
        
        if response == False:
            return

        for garbage_info in garbage_list:
            if garbage_info.checkbutton_variable.get() == False:
                continue

            result = garbage_info.fix.execute()

            if result:
                # Show error message
                messagebox.showwarning("Fehler", 
                                       "Mindestens eine Option benötigt erweiterte Rechte.\n"
                                       "Bitte starte das Programm mit Administratorrechten neu oder ändere die Auswahl.")
                return
        
        # Show success message
        messagebox.showinfo("You're set!", "Alle ausgewählten Optionen wurden erfolgreich ausgeführt.")

    @staticmethod
    def is_admin():
        try:
            is_admin = os.getuid() == 0
        except AttributeError:
            is_admin = ctypes.windll.shell32.IsUserAnAdmin()
        return is_admin
    
    @staticmethod
    def resource_path(relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)

if __name__ == "__main__":
    garbage_list: tuple[str, GarbageInfo, None] = [    
        RemoveAppPackageGarbageInfo("Clipchamp", "Clipchamp.Clipchamp"),
        RemoveAppPackageGarbageInfo("Cortana", "Microsoft.549981C3F5F10"),
        RemoveAppPackageGarbageInfo("Microsoft News", "Microsoft.BingNews"),
        RemoveAppPackageGarbageInfo("Wetter", "Microsoft.BingWeather"),
        RemoveAppPackageGarbageInfo("Xbox", "Microsoft.GamingApp"),
        RemoveAppPackageGarbageInfo("Hilfe anfordern", "Microsoft.GetHelp"),
        RemoveAppPackageGarbageInfo("Getstarted!!!", "Microsoft.Getstarted"), # erste schritte ist's nicht
        RemoveAppPackageGarbageInfo("HEIF Image Extension!!!", "Microsoft.HEIFImageExtension"),
        RemoveAppPackageGarbageInfo("HEVC Video Extension!!!", "Microsoft.HEVCVideoExtension"),
        RemoveAppPackageGarbageInfo("Office", "Microsoft.MicrosoftOfficeHub"),
        RemoveAppPackageGarbageInfo("Solitaire Collection", "Microsoft.MicrosoftSolitaireCollection"),
        RemoveAppPackageGarbageInfo("Kurznotizen", "Microsoft.MicrosoftStickyNotes"),
        RemoveAppPackageGarbageInfo("Paint", "Microsoft.Paint"),
        RemoveAppPackageGarbageInfo("People!!!", "Microsoft.People"),
        RemoveAppPackageGarbageInfo("Power Automate", "Microsoft.PowerAutomateDesktop"),
        RemoveAppPackageGarbageInfo("Raw Image Extension!!!", "Microsoft.RawImageExtension"),
        RemoveAppPackageGarbageInfo("Snipping Tool", "Microsoft.ScreenSketch"),
        RemoveAppPackageGarbageInfo("Store Purchase App!!!", "Microsoft.StorePurchaseApp"), # nicht store
        RemoveAppPackageGarbageInfo("Microsoft To Do", "Microsoft.Todos"),
        RemoveAppPackageGarbageInfo("VP9 Video Extensions!!!", "Microsoft.VP9VideoExtensions"),
        RemoveAppPackageGarbageInfo("Web Media Extensions!!!", "Microsoft.WebMediaExtensions"),
        RemoveAppPackageGarbageInfo("Webp Image Extension!!!", "Microsoft.WebpImageExtension"),
        RemoveAppPackageGarbageInfo("Windows-Fotoanzeige", "Microsoft.Windows.Photos"),
        RemoveAppPackageGarbageInfo("Alarm und Uhr", "Microsoft.WindowsAlarms"),
        RemoveAppPackageGarbageInfo("Rechner", "Microsoft.WindowsCalculator"),
        RemoveAppPackageGarbageInfo("Kamera", "Microsoft.WindowsCamera"),
        RemoveAppPackageGarbageInfo("MS Windows Communications Apps!!!", "microsoft.windowscommunicationsapps"),
        RemoveAppPackageGarbageInfo("Feedback-Hub", "Microsoft.WindowsFeedbackHub"),
        RemoveAppPackageGarbageInfo("Karten", "Microsoft.WindowsMaps"),
        RemoveAppPackageGarbageInfo("Editor", "Microsoft.WindowsNotepad"), # not wordpad
        RemoveAppPackageGarbageInfo("Sprachrekorder", "Microsoft.WindowsSoundRecorder"),
        RemoveAppPackageGarbageInfo("Store", "Microsoft.WindowsStore"),
        RemoveAppPackageGarbageInfo("Terminal", "Microsoft.WindowsTerminal"),
        RemoveAppPackageGarbageInfo("Xbox Live", "Microsoft.Xbox.TCUI"),
        RemoveAppPackageGarbageInfo("Xbox Game Overlay!!!", "Microsoft.XboxGameOverlay"),
        RemoveAppPackageGarbageInfo("Xbox Game Bar", "Microsoft.XboxGamingOverlay"),
        RemoveAppPackageGarbageInfo("Xbox Identity Provider!!!", "Microsoft.XboxIdentityProvider"),
        RemoveAppPackageGarbageInfo("Xbox Speech To Text Overlay!!!", "Microsoft.XboxSpeechToTextOverlay"),
        RemoveAppPackageGarbageInfo("Smartphone-Link", "Microsoft.YourPhone"),
        RemoveAppPackageGarbageInfo("Windows Media Player Legacy", "Microsoft.ZuneMusic"),
        RemoveAppPackageGarbageInfo("Filme und TV", "Microsoft.ZuneVideo"),
        RemoveAppPackageGarbageInfo("Family", "MicrosoftCorporationII.MicrosoftFamily"),
        RemoveAppPackageGarbageInfo("Remotehilfe", "MicrosoftCorporationII.QuickAssist"),
        RemoveAppPackageGarbageInfo("Teams", "MicrosoftTeams"), # tips, spotify, onedrive, erste schritte
        RemoveAppPackageGarbageInfo("Web Experience!!!", "MicrosoftWindows.Client.WebExperience"),
        GarbageInfo(None, 
                    "Autostart Apps deaktivieren", 
                    "Deaktiviert alle Apps aus dem Autostart, entfernt sie aber nicht. Gleich deaktivierter Apps im Task-Manager.", 
                    ClearAutostart()),
        GarbageInfo("Datei Explorer", "Dateinamenerweiterungen immer anzeigen", "Zeigt den Dateitypen für jede Datei im Explorer.", ShowFileExtensions()),
        GarbageInfo("Datei Explorer", "Versteckte Dateien anzeigen", "Macht auch versteckte Dateien im Explorer sichtbar.", ShowHiddenFiles()),
    ]

    root = Tk()
    MainWindow(root)
    root.mainloop()