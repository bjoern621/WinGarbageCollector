from dataclasses import dataclass
from GarbageFix import GarbageFix
from RemoveAppPackage import RemoveAppPackage

@dataclass
class GarbageInfo:
    name: str
    description: str
    warning: bool
    fix: GarbageFix

class RemoveAppPackageGarbageInfo(GarbageInfo):
    def __init__(self, display_name: str, package_name: str, warning: bool = False) -> None:
        self.name = f"{display_name} entfernen"
        self.description = f"Diese Option deinstalliert {display_name}, wenn {display_name} installiert ist."
        self.warning = warning
        self.fix = RemoveAppPackage(package_name)