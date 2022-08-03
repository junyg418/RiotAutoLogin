import subprocess
from GuiClassFile import PathErrorGui

riot_clint_path = "C:\Riot Games\Riot Client\RiotClienServices.exe"

try:
    subprocess.check_output(riot_clint_path, shell=True)
except:
    PathErrorGui.open_error_page()