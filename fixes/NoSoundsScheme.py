import winreg
from GarbageFix import GarbageFix

class NoSoundsScheme(GarbageFix):
    def execute(self):
        registry_path = r"AppEvents\Schemes"
        preferred_value = ".None"

        try:
            open_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, registry_path, 0, winreg.KEY_SET_VALUE)
        except PermissionError:
            return 1

        winreg.SetValueEx(open_key, None, 0, winreg.REG_SZ, preferred_value)
        winreg.CloseKey(open_key)

        self.set_subkey_values();

        return 0
    
    @staticmethod
    def set_subkey_values():
        apps_path = r"AppEvents\Schemes\Apps"
        set_value = ""
        
        try:
            open_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, apps_path, 0, winreg.KEY_READ)

            i = 0
            while True:
                try:
                    sub_key = winreg.EnumKey(open_key, i)

                    open_key_2 = winreg.OpenKey(winreg.HKEY_CURRENT_USER, apps_path + fr"\{sub_key}", 0, winreg.KEY_READ)

                    i1 = 0
                    while True:
                        try:
                            my_key = winreg.EnumKey(open_key_2, i1)

                            open_key_3 = winreg.OpenKey(winreg.HKEY_CURRENT_USER, apps_path + fr"\{sub_key}\{my_key}\.Current", 0, winreg.KEY_SET_VALUE)
                            winreg.SetValueEx(open_key_3, None, 0, winreg.REG_SZ, set_value)

                            winreg.CloseKey(open_key_3)
                        except PermissionError:
                            return 1
                        except OSError:
                            break

                        i1 += 1
                except PermissionError:
                    return 1
                except OSError:
                    break

                i += 1

            winreg.CloseKey(open_key)
        except PermissionError:
            return 1

        return 0
