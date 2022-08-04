import pyautogui

#400,360
#240,200
#320,200
"""
클라이언트 규격
2560*1440 (125%)
1920*1080(100% defult)
1596*898(지원x?)
"""
def find_locate(size:tuple=(1920,1080)) -> tuple:
    locate_sign = pyautogui.locateOnScreen(f'./img/login_img({size[0]}_{size[1]}).jpg',confidence = 0.6)
    while locate_sign == None:
        locate_sign = pyautogui.locateOnScreen(f'./img/login_img({size[0]}_{size[1]}).jpg',confidence = 0.6)
    return (locate_sign[0],locate_sign[1]) # (left, top)

def click_id(locate:tuple):
    pyautogui.moveTo((locate[0]+200,locate[1]+240))
    # pyautogui.click((locate[0]+240,locate[1]+200))
    print('아클릭')

def click_passward(locate:tuple):
    pyautogui.click((locate[0]+200,locate[1]+320))
    print('비클릭')


if __name__ == '__main__':
    locate = find_locate()
    # click_id(locate)
    click_passward(locate)