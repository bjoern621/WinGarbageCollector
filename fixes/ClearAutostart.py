import winreg
from GarbageFix import GarbageFix

class ClearAutostart(GarbageFix):
    def execute(self):
        startup_approved_run_path = r"Software\Microsoft\Windows\CurrentVersion\Explorer\StartupApproved\Run"
        startup_approved_run32_path = r"Software\Microsoft\Windows\CurrentVersion\Explorer\StartupApproved\Run32"
        startup_approved_folder_path = r"Software\Microsoft\Windows\CurrentVersion\Explorer\StartupApproved\StartupFolder"

        # alternative_startup_approved_run_path = r"Microsoft\Windows\CurrentVersion\Explorer\StartupApproved\Run"

        if self.set_key_values(winreg.HKEY_CURRENT_USER, startup_approved_run_path):
            return 1
        if self.set_key_values(winreg.HKEY_CURRENT_USER, startup_approved_folder_path):
            return 1

        if self.set_key_values(winreg.HKEY_LOCAL_MACHINE, startup_approved_run_path):
            return 1
        if self.set_key_values(winreg.HKEY_LOCAL_MACHINE, startup_approved_run32_path):
            return 1
        if self.set_key_values(winreg.HKEY_LOCAL_MACHINE, startup_approved_folder_path):
            return 1

        return 0

    @staticmethod
    def set_key_values(key, sub_key):
        inactive_value = b"\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
        try:
            open_key = winreg.OpenKey(key, sub_key, 0, winreg.KEY_READ | winreg.KEY_SET_VALUE)
        except PermissionError:
            return 1

        i = 0
        while True:
            try:
                sub_value = winreg.EnumValue(open_key, i)

                winreg.SetValueEx(open_key, sub_value[0], 0, winreg.REG_BINARY, inactive_value)
            except PermissionError:
                return 1
            except OSError:
                break

            i += 1

        winreg.CloseKey(open_key)

        return 0
