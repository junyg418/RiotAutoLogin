from os import startfile
from CsvDataProcessingModule import get_path
from GuiClassFile import PathErrorGui


# riot_clint_path = "C:\Riot Games\Riot Client\RiotClientServices.ex"

# 기존 run 함수 제거
# > 사유: 프로그램이 종료됨과 상관없이 실행되야하는데 subprocess 모듈과는 알맞지 않기에 변경함
# def run() -> None:
#     """
#     라이엇 클라이언트 실행시키는 함수  -> subprocess 모듈 사용
#     """
#     path = get_path()  # import CsvDataProcessingModule
#     try:
#         subprocess.run(path, shell=True)
#         # subprocess.check_output(path, shell=True)
#     except subprocess.CalledProcessError:
#         PathErrorGui.open_error_page()

def run() -> None:
    """
    라이엇 클라이언트 실행시키는 함수
    """
    path = get_path()
    try:
        startfile(path)  # -> os 모듈
    except FileNotFoundError:
        PathErrorGui.open_error_page()


if __name__ == '__main__':
    run()
