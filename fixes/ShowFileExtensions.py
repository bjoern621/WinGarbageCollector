import winreg
from GarbageFix import GarbageFix

class ShowFileExtensions(GarbageFix):
    def execute(self):
        registry_path = r"Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced"
        preferred_value = 0

        try:
            open_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, registry_path, 0, winreg.KEY_SET_VALUE)
        except PermissionError:
            return 1

        winreg.SetValueEx(open_key, "HideFileExt", 0, winreg.REG_DWORD, preferred_value)

        winreg.CloseKey(open_key)

        return 0
