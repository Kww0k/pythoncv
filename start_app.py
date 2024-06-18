import cv2
import mss
import numpy as np
import psutil
import pyautogui

arr = {"left": 0, "top": 0, "width": 2160, "height": 1280}


def is_process_running(process_name):
    for proc in psutil.process_iter(['name']):
        try:
            if process_name.lower() in proc.info['name'].lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False


def getLab(tool, img):
    pic = tool.grab(arr)
    pic = np.array(pic)
    gray_level = cv2.cvtColor(pic, cv2.COLOR_BGR2GRAY)

    search = cv2.imread(img)
    search_gray_level = cv2.cvtColor(search, cv2.COLOR_BGR2GRAY)

    compare = cv2.matchTemplate(gray_level, search_gray_level, cv2.TM_CCOEFF_NORMED)

    filtration = np.where(compare >= 0.85)
    result = list(zip(*filtration[::-1]))

    if len(result) > 0:
        # 提取 x 和 y 值
        x_values = [coord[0] for coord in result]
        y_values = [coord[1] for coord in result]
        # 计算 x 和 y 的总和
        sum_x = sum(x_values)
        sum_y = sum(y_values)
        # 计算 x 和 y 的平均值
        average_x = sum_x / len(result) if result else float('nan')
        average_y = sum_y / len(result) if result else float('nan')
        return average_x, average_y
    else:
        return None, None


with mss.mss() as sct:
    is_have_app = False
    while True:
        if is_process_running('wemeetapp.exe'):
            is_have_app = True
            break
        x, y = getLab(sct, "img/app.png")
        if x and y:
            pyautogui.doubleClick(x=x, y=y)
            is_have_app = True
            break

    ready_to_login = False
    if is_have_app:
        while True:
            x, y = getLab(sct, "img/login.png")
            if x and y:
                print("已登录")
            x, y = getLab(sct, "img/phoneLogin.png")
            if x and y:
                pyautogui.click(x=x, y=y)
                ready_to_login = True
                break

    phone_ready = False
    if ready_to_login:
        while True:
            x, y = getLab(sct, "img/phone.png")
            if x and y:
                pyautogui.click(x=x, y=y)
                pyautogui.typewrite("19858591692")
                pyautogui.press("tab")
                pyautogui.typewrite("2503841.Sb")
                phone_ready = True
                break

    if phone_ready:
        while True:
            x, y = getLab(sct, "img/login.png")
            if x and y:
                pyautogui.click(x=x, y=y)
                break
