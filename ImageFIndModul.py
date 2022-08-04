import pyautogui


locate_passward = pyautogui.locateCenterOnScreen('./img/passward_img.png')

def id_click():
    locate_id = pyautogui.locateCenterOnScreen('./img/id_img.png', confidence=0.7)
    while locate_id == None:
        locate_id = pyautogui.locateCenterOnScreen('./img/id_img.png', confidence=0.7)
        print('다시')
    pyautogui.moveTo(locate_id)
    # pyautogui.click(locate_id)
    print('클릭')

id_click()