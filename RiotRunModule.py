import subprocess
from CsvDataProcessingModule import get_path
from GuiClassFile import PathErrorGui

riot_clint_path = "C:\Riot Games\Riot Client\RiotClientServices.exe"


def run_riot_clint() -> None:
    path = get_path()  # import CsvDataProcessingModule
    try:
        subprocess.check_output(path, shell=True)
    except subprocess.CalledProcessError:
        PathErrorGui.open_error_page()


if __name__ == '__main__':
    run_riot_clint()
