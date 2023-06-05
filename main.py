import ctypes
import os
from tkinter import *
from tkinter import ttk
from GarbageInfo import *
from ScrollArea import ScrollArea

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
        root.iconbitmap("images/bin.ico")

        # Main frame
        main_frame = ttk.Frame(root).pack()

        # Scroll area
        ScrollArea(main_frame, garbage_list).pack(expand=True, fill=BOTH)

        # Button area
        button_frame = ttk.Frame(main_frame, style="button_frame.TFrame", padding=(0, 7.5, 7.5, 7.5))

        ttk.Button(button_frame, text="Beenden", command=lambda: root.quit(), style="button_frame.TButton", takefocus=False).pack(side=RIGHT, padx=(7.5, 0))
        ttk.Button(button_frame, text="Bestätigen", style="button_frame.TButton", takefocus=False).pack(side=RIGHT)

        button_frame.pack(fill=X)

        # Styling
        s = ttk.Style(main_frame)
        s.configure("button_frame.TFrame", background="lightgrey")
        s.configure("button_frame.TButton", background="lightgrey")

    @staticmethod
    def is_admin():
        try:
            is_admin = os.getuid() == 0
        except AttributeError:
            is_admin = ctypes.windll.shell32.IsUserAnAdmin()
        return is_admin

if __name__ == "__main__":
    garbage_list = [
        ("Programme deinstallieren", RemoveAppPackageGarbageInfo("Clipchamp", "Clipchamp.Clipchamp"), None),
        ("Programme deinstallieren", RemoveAppPackageGarbageInfo("Cortana", "Microsoft.549981C3F5F10")),
        ("Programme deinstallieren", RemoveAppPackageGarbageInfo("Microsoft News", "Microsoft.BingNews")),
        ("Programme deinstallieren", RemoveAppPackageGarbageInfo("Wetter", "Microsoft.BingWeather")),
        ("Programme deinstallieren", RemoveAppPackageGarbageInfo("Xbox", "Microsoft.GamingApp")),
        ("Programme deinstallieren", RemoveAppPackageGarbageInfo("Hilfe anfordern", "Microsoft.GetHelp")),
        ("Programme deinstallieren", RemoveAppPackageGarbageInfo("Getstarted!!!", "Microsoft.Getstarted")), # erste schritte ist's nicht
        ("Programme deinstallieren", RemoveAppPackageGarbageInfo("HEIF Image Extension!!!", "Microsoft.HEIFImageExtension")),
        ("Programme deinstallieren", RemoveAppPackageGarbageInfo("HEVC Video Extension!!!", "Microsoft.HEVCVideoExtension")),
        ("Programme deinstallieren", RemoveAppPackageGarbageInfo("Office", "Microsoft.MicrosoftOfficeHub")),
        ("Programme deinstallieren", RemoveAppPackageGarbageInfo("Solitaire Collection", "Microsoft.MicrosoftSolitaireCollection")),
        ("Programme deinstallieren", RemoveAppPackageGarbageInfo("Kurznotizen", "Microsoft.MicrosoftStickyNotes")),
        ("Programme deinstallieren", RemoveAppPackageGarbageInfo("Paint", "Microsoft.Paint")),
        ("Programme deinstallieren", RemoveAppPackageGarbageInfo("People!!!", "Microsoft.People")),
        ("Programme deinstallieren", RemoveAppPackageGarbageInfo("Power Automate", "Microsoft.PowerAutomateDesktop")),
        ("Programme deinstallieren", RemoveAppPackageGarbageInfo("Raw Image Extension!!!", "Microsoft.RawImageExtension")),
        ("Programme deinstallieren", RemoveAppPackageGarbageInfo("Snipping Tool", "Microsoft.ScreenSketch")),
        ("Programme deinstallieren", RemoveAppPackageGarbageInfo("Store Purchase App!!!", "Microsoft.StorePurchaseApp")), # nicht store
        ("Programme deinstallieren", RemoveAppPackageGarbageInfo("Microsoft To Do", "Microsoft.Todos")),
        ("Programme deinstallieren", RemoveAppPackageGarbageInfo("VP9 Video Extensions!!!", "Microsoft.VP9VideoExtensions")),
        ("Programme deinstallieren", RemoveAppPackageGarbageInfo("Web Media Extensions!!!", "Microsoft.WebMediaExtensions")),
        ("Programme deinstallieren", RemoveAppPackageGarbageInfo("Webp Image Extension!!!", "Microsoft.WebpImageExtension")),
        ("Programme deinstallieren", RemoveAppPackageGarbageInfo("Windows-Fotoanzeige", "Microsoft.Windows.Photos")),
        ("Programme deinstallieren", RemoveAppPackageGarbageInfo("Alarm und Uhr", "Microsoft.WindowsAlarms")),
        ("Programme deinstallieren", RemoveAppPackageGarbageInfo("Rechner", "Microsoft.WindowsCalculator")),
        ("Programme deinstallieren", RemoveAppPackageGarbageInfo("Kamera", "Microsoft.WindowsCamera")),
        ("Programme deinstallieren", RemoveAppPackageGarbageInfo("MS Windows Communications Apps!!!", "microsoft.windowscommunicationsapps")),
        ("Programme deinstallieren", RemoveAppPackageGarbageInfo("Feedback-Hub", "Microsoft.WindowsFeedbackHub")),
        ("Programme deinstallieren", RemoveAppPackageGarbageInfo("Karten", "Microsoft.WindowsMaps")),
        ("Programme deinstallieren", RemoveAppPackageGarbageInfo("Editor", "Microsoft.WindowsNotepad")), # not wordpad
        ("Programme deinstallieren", RemoveAppPackageGarbageInfo("Sprachrekorder", "Microsoft.WindowsSoundRecorder")),
        ("Programme deinstallieren", RemoveAppPackageGarbageInfo("Store", "Microsoft.WindowsStore")),
        ("Programme deinstallieren", RemoveAppPackageGarbageInfo("Terminal", "Microsoft.WindowsTerminal")),
        ("Programme deinstallieren", RemoveAppPackageGarbageInfo("Xbox Live", "Microsoft.Xbox.TCUI")),
        ("Programme deinstallieren", RemoveAppPackageGarbageInfo("Xbox Game Overlay!!!", "Microsoft.XboxGameOverlay")),
        ("Programme deinstallieren", RemoveAppPackageGarbageInfo("Xbox Game Bar", "Microsoft.XboxGamingOverlay")),
        ("Programme deinstallieren", RemoveAppPackageGarbageInfo("Xbox Identity Provider!!!", "Microsoft.XboxIdentityProvider")),
        ("Programme deinstallieren", RemoveAppPackageGarbageInfo("Xbox Speech To Text Overlay!!!", "Microsoft.XboxSpeechToTextOverlay")),
        ("Programme deinstallieren", RemoveAppPackageGarbageInfo("Ihr Smartphone", "Microsoft.YourPhone")),
        ("Programme deinstallieren", RemoveAppPackageGarbageInfo("Windows Media Player Lagecy", "Microsoft.ZuneMusic")),
        ("Programme deinstallieren", RemoveAppPackageGarbageInfo("Filme und TV", "Microsoft.ZuneVideo")),
        ("Programme deinstallieren", RemoveAppPackageGarbageInfo("Family", "MicrosoftCorporationII.MicrosoftFamily")),
        ("Programme deinstallieren", RemoveAppPackageGarbageInfo("Remotehilfe", "MicrosoftCorporationII.QuickAssist")),
        ("Programme deinstallieren", RemoveAppPackageGarbageInfo("Teams", "MicrosoftTeams")), # tips, spotify, onedrive, erste schritte
        ("Programme deinstallieren", RemoveAppPackageGarbageInfo("Web Experience!!!", "MicrosoftWindows.Client.WebExperience"))
    ]

    root = Tk()
    MainWindow(root)
    root.mainloop()