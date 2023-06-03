import subprocess
from GarbageFix import GarbageFix

class RemoveAppPackage(GarbageFix):
    def __init__(self, package_name):
        self.package_name = package_name
        self.administrator_privileges_required = True

    def execute(self):
        print(self.package_name)
        completed = subprocess.run(
            ["powershell", "-Command", f"Get-AppxPackage -allusers -name *{self.package_name}* | Remove-AppxPackage -allusers"])
        return completed.returncode
