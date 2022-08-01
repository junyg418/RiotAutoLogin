import subprocess

riot_clint_path = "C:\Riot Games\Riot Client\RiotClientServices.exe"

try:
    subprocess.check_output(riot_clint_path, shell=True)
except:
    print('경로 이상')  # TODO 경고 매세지 추가 예정
