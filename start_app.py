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


with mss.mss() as sct:
    is_have_app = False
    while True:
        if is_process_running('wemeetapp.exe'):
            is_have_app = True
            break
        pic = sct.grab(arr)
        pic = np.array(pic)
        huidu = cv2.cvtColor(pic, cv2.COLOR_BGR2GRAY)

        to = cv2.imread("img/app.png")
        to_huidu = cv2.cvtColor(to, cv2.COLOR_BGR2GRAY)

        chazhao = cv2.matchTemplate(huidu, to_huidu, cv2.TM_CCOEFF_NORMED)

        shaixuan = np.where(chazhao >= 0.85)
        liebiao = list(zip(*shaixuan[::-1]))

        if len(liebiao) > 0:
            # 提取 x 和 y 值
            x_values = [coord[0] for coord in liebiao]
            y_values = [coord[1] for coord in liebiao]

            # 计算 x 和 y 的总和
            sum_x = sum(x_values)
            sum_y = sum(y_values)

            # 计算 x 和 y 的平均值
            average_x = sum_x / len(liebiao) if liebiao else float('nan')
            average_y = sum_y / len(liebiao) if liebiao else float('nan')

            print(average_x, average_y)
            pyautogui.doubleClick(average_x, average_y)
        else:
            print("没有相似的")

    ready_to_login = False
    if is_have_app:
        while True:
            pic = sct.grab(arr)
            pic = np.array(pic)
            huidu = cv2.cvtColor(pic, cv2.COLOR_BGR2GRAY)

            is_login = cv2.imread("img/logined.png")
            is_login_huidu = cv2.cvtColor(is_login, cv2.COLOR_BGR2GRAY)
            chazhao = cv2.matchTemplate(huidu, is_login_huidu, cv2.TM_CCOEFF_NORMED)
            shaixuan = np.where(chazhao >= 0.85)
            liebiao = list(zip(*shaixuan[::-1]))
            if len(liebiao) > 0:
                print("已登录")
                break

            to = cv2.imread("img/phoneLogin.png")
            to_huidu = cv2.cvtColor(to, cv2.COLOR_BGR2GRAY)

            chazhao = cv2.matchTemplate(huidu, to_huidu, cv2.TM_CCOEFF_NORMED)

            shaixuan = np.where(chazhao >= 0.85)
            liebiao = list(zip(*shaixuan[::-1]))

            if len(liebiao) > 0:
                # 提取 x 和 y 值
                x_values = [coord[0] for coord in liebiao]
                y_values = [coord[1] for coord in liebiao]

                # 计算 x 和 y 的总和
                sum_x = sum(x_values)
                sum_y = sum(y_values)

                # 计算 x 和 y 的平均值
                average_x = sum_x / len(liebiao) if liebiao else float('nan')
                average_y = sum_y / len(liebiao) if liebiao else float('nan')

                print(average_x, average_y)
                pyautogui.click(average_x, average_y)
                ready_to_login = True
                break
            else:
                print("没有相似的")

    phone_ready = False
    if ready_to_login:
        while True:
            pic = sct.grab(arr)
            pic = np.array(pic)
            huidu = cv2.cvtColor(pic, cv2.COLOR_BGR2GRAY)

            to = cv2.imread("img/phone.png")
            to_huidu = cv2.cvtColor(to, cv2.COLOR_BGR2GRAY)

            chazhao = cv2.matchTemplate(huidu, to_huidu, cv2.TM_CCOEFF_NORMED)

            shaixuan = np.where(chazhao >= 0.85)
            liebiao = list(zip(*shaixuan[::-1]))

            if len(liebiao) > 0:
                # 提取 x 和 y 值
                x_values = [coord[0] for coord in liebiao]
                y_values = [coord[1] for coord in liebiao]

                # 计算 x 和 y 的总和
                sum_x = sum(x_values)
                sum_y = sum(y_values)

                # 计算 x 和 y 的平均值
                average_x = sum_x / len(liebiao) if liebiao else float('nan')
                average_y = sum_y / len(liebiao) if liebiao else float('nan')

                print(average_x, average_y)
                pyautogui.click(average_x, average_y)
                pyautogui.typewrite("your phone")
                pyautogui.press("tab")
                pyautogui.typewrite("your password")
                phone_ready = True
                break
            else:
                print("没有相似的")

    if phone_ready:
        while True:
            pic = sct.grab(arr)
            pic = np.array(pic)
            huidu = cv2.cvtColor(pic, cv2.COLOR_BGR2GRAY)

            to = cv2.imread("img/login.png")
            to_huidu = cv2.cvtColor(to, cv2.COLOR_BGR2GRAY)

            chazhao = cv2.matchTemplate(huidu, to_huidu, cv2.TM_CCOEFF_NORMED)

            shaixuan = np.where(chazhao >= 0.85)
            liebiao = list(zip(*shaixuan[::-1]))

            if len(liebiao) > 0:
                # 提取 x 和 y 值
                x_values = [coord[0] for coord in liebiao]
                y_values = [coord[1] for coord in liebiao]

                # 计算 x 和 y 的总和
                sum_x = sum(x_values)
                sum_y = sum(y_values)

                # 计算 x 和 y 的平均值
                average_x = sum_x / len(liebiao) if liebiao else float('nan')
                average_y = sum_y / len(liebiao) if liebiao else float('nan')

                print(average_x, average_y)
                pyautogui.click(average_x, average_y)
                break
            else:
                print("没有相似的")
