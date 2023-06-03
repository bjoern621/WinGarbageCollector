from dataclasses import dataclass
from GarbageFix import GarbageFix
from RemoveAppPackage import RemoveAppPackage

@dataclass
class GarbageInfo:
    name: str
    description: str
    high_impact: bool
    fix: GarbageFix

class RemoveAppPackageGarbageInfo(GarbageInfo):
    def __init__(self, display_name: str, package_name: str, high_impact: bool) -> None:
        self.name = f"{display_name} entfernen"
        self.description = f"Diese Option deinstalliert {display_name}, wenn {display_name} installiert ist."
        self.high_impact = high_impact
        self.fix = RemoveAppPackage(package_name)