import pyautogui

# 400,360
# 240,200
# 320,200
"""
클라이언트 규격
2560*1440 (125%) 지원 x
1920*1080(100% default)
1596*898(지원x?)
"""


def find_locate(size: tuple = (1920, 1080)) -> tuple:
    """
    아이디, 비밀번호 입력칸 좌표 찾는 함수
    :return:
        tuple->(raw, column)
    """
    locate_sign = pyautogui.locateOnScreen(f'./img/login_img({size[0]}_{size[1]}).jpg', confidence=0.6)
    while locate_sign is None:
        locate_sign = pyautogui.locateOnScreen(f'./img/login_img({size[0]}_{size[1]}).jpg', confidence=0.6)
    return locate_sign[0], locate_sign[1]


def click_id(block_location: tuple) -> None:
    """
    click to id input field

    :param block_location:
        input field location -> (raw, column)
    :return:
        None
    """
    pyautogui.click((block_location[0] + 200, block_location[1] + 240))


def click_password(block_location: tuple) -> None:
    """
    click to password input field

    :param block_location:
        input field location -> (raw, column)
    :return:
        None
    """
    pyautogui.click((block_location[0] + 200, block_location[1] + 320))


if __name__ == '__main__':
    locate = find_locate()
    click_id(locate)
    click_password(locate)
