import subprocess
from GuiClassFile import PathErrorGui


# def run_riot_clint(path):
#     try:
#         subprocess.check_output(path, shell=True)
#     except:
#         PathErrorGui.open_error_page()
riot_clint_path = "C:\Riot Games\Riot Client\RiotClientServices.exe"
riot_clint_path = "C:\Riot Games\Riot Client\RiotClientService.exe"
def run():
    # try:
    subprocess.check_output(riot_clint_path, shell=True)
    # except:
    #     PathErrorGui.open_error_page()

if __name__ == '__main__':
    run()