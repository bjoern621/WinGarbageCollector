from dataclasses import dataclass
from tkinter import IntVar
from GarbageFix import GarbageFix
from fixes.RemoveAppPackage import RemoveAppPackage

@dataclass
class GarbageInfo:
    parent_checkbox_name: str
    name: str
    description: str
    fix: GarbageFix
    checkbutton_variable: IntVar = None
    warning: bool = False

class RemoveAppPackageGarbageInfo(GarbageInfo):
    def __init__(self, display_name: str, package_name: str) -> None:
        super().__init__("Programme deinstallieren", 
                         f"{display_name} entfernen", 
                         f"Diese Option deinstalliert {display_name}, wenn {display_name} installiert ist.", 
                         RemoveAppPackage(package_name))