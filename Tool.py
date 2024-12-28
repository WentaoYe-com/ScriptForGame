import os
from PIL import Image
from mouseinfo import position

import Click_position_obtain
import AutoClick
import pyautogui
import time
from pynput import mouse
from pynput import keyboard
import cv2
import numpy as np

def locate_image(image_filename, confidence=0.8, debug_mode = 0):
    """
    在屏幕上找到给定图片的位置。

    参数:
    image_path (str): 图片文件的路径
    confidence (float): 匹配的最低置信度,默认为 0.8

    返回:
    (x, y, w, h) 或 None: 如果找到匹配项,返回图片在屏幕上的位置;否则返回 None
    """
    try:
        # 获取脚本所在目录的路径
        script_dir = os.path.dirname(os.path.abspath(__file__))

        # 拼接图片文件的完整路径
        image_path = os.path.join(script_dir, image_filename)

        # Debug: Print the image path
        if debug_mode:
            print(f"Image path: {image_path}")
        try:
            image = Image.open(image_path)
            bit_depth = image.mode
            if debug_mode:
                print(f"The bit depth of the image '{image_path}' is {bit_depth}.")
        except Exception as e:
            print(f"Error: {str(e)}")

        # 读取图片
        template = cv2.imread(image_path)
        if template is None:
            print(f"Error: Unable to load image at {image_path}")
            return None

        # If the image has an alpha channel, convert it to RGB
        if template.shape[2] == 4:  # Check for 4 channels (RGBA)
            template = cv2.cvtColor(template, cv2.COLOR_BGRA2BGR)
            # print("Converted image from RGBA to BGR.")

        # 截取整个屏幕
        pyautogui.screenshot().save("screenshot.png")  # 保存到当前工作目录
        if debug_mode:
            print("Screenshot saved as 'screenshot.png'.")
        image_path2 = os.path.join(script_dir, "screenshot.png")
        screen = cv2.imread(image_path2)

        # 在屏幕上查找图片
        res = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(res)

        # 检查是否找到匹配项
        if max_val >= confidence:
            return max_loc[0], max_loc[1], template.shape[1], template.shape[0]
        else:
            return None

    except FileNotFoundError:
        print(f"Error: The image file 'target.png' could not be found.")
        return None
    except Exception as e:
        print(f"Error: {str(e)}")
        return None

def click_position_record():
    def on_click(x, y, button, pressed):
        nonlocal click_positions
        if button == mouse.Button.left and pressed:
            print(f"左键点击位置 ({x}, {y})")
            click_positions.append((x, y))
        elif button == mouse.Button.right and pressed:
            print("右键触发。 结束录制...")
            listener.stop()

    listener = mouse.Listener(on_click=on_click)
    click_positions = []  # 存储鼠标点击位置的列表
    listener.start()
    print("记录左键点击的位置，右键结束记录...")
    listener.join()
    return click_positions

def auto_click(positions, interval=-1):
    if interval == -1:
        interval = [0.1] * len(positions)
    should_exit = False
    def on_press(key):
        nonlocal should_exit
        if key == keyboard.Key.f12:
            print("F12 按下, 结束连点...")
            should_exit = True
            return False

    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    try:
        while not should_exit:
            # 获取鼠标当前位置
            for i in range(len(positions)):
                x, y = int(positions[i][0]), int(positions[i][1])
                # 在当前位置点击鼠标左键
                pyautogui.click(x, y)
                print(f"已在({x}, {y})位置点击")
                # 等待下次点击
                time.sleep(interval[i])
        listener.stop()
        print("停止自动点击")
    except KeyboardInterrupt:
        print("停止自动点击")

def locate_error_report(location=None, error_explain='error'):
    if location == None:
        print(error_explain)
        exit()

def position_cal(location):
    position = (location[0] + location[3] / 2, location[1] + location[2] / 2)
    x, y = int(position[0]), int(position[1])
    return x, y

def enter_field_page():
    '''
    进入野外界面
    :return: 无
    '''
    location_yewai = locate_image(r'Figures\field.png', 0.80)
    if location_yewai != None:
        x, y = position_cal(location_yewai)
        pyautogui.click(x, y)
        location_chengzhen = locate_image(r'Figures\chengzhen.png', 0.80)
        while location_chengzhen == None:
            location_chengzhen = locate_image(r'Figures\chengzhen.png', 0.80)
        time.sleep(1)
        print('进入野外界面')
    else:
        print('已在野外界面')

def page_judge():
    location_yewai = locate_image(r'Figures\field.png', 0.80)
    location_chengzhen = locate_image(r'Figures\chengzhen.png', 0.80)
    # 判断在哪个界面：城镇 或者 野外
    if location_yewai != None:
        print('目前界面在城镇')
        return 0
    else:
        if location_chengzhen != None:
            print('目前界面在野外')
            return 1
        else:
            print('目前界面既不在城镇也不在野外')
            return 2

def enter_intelligence_page():
    """
        从野外界面进入情报界面，如果成功则返回游戏界面左下角坐标，否则退出程序。

        返回: （x, y） 游戏界面左下端坐标

    """
    location = locate_image(r'Figures\qingbao.png', 0.80)
    if location == None:
        location = locate_image(r'Figures\qingbao_2.png', 0.80)
    if location != None:
        x, y = position_cal(location)
        pyautogui.click(x, y)
        time.sleep(2)
        # 检测是否进入情报页面
        location_qingbaojiemian = locate_image(r'Figures\qingbaojiemian.png', 0.80)
        if location_qingbaojiemian == None:
            print("未进入情报界面")
            exit()
        # 定位页面左下角
        x_0, y_0 = location_qingbaojiemian[0] - 25, location_qingbaojiemian[1] + 10
        # x, y = position_cal(location_qingbaojiemian)
        # pyautogui.click(x, y)
        # pyautogui.click(x_0, y_0)
        # print(x, y)
        # print(x_0, y_0)
        print('进入情报界面')
        return (x_0, y_0)
    else:
        print('进入情报界面时出错')
        exit()

def random_time(delay=1):
    return delay + np.random.uniform(0, 0.5)

def left_click(location, delay):
    x, y = position_cal(location)
    pyautogui.click(x, y)
    time.sleep(random_time(delay))

if __name__ == '__main__':
    location = locate_image(r'Figures\field.png',0.80)
    print(location)
    positions = [(location[0]+location[3]/2, location[1]+location[2]/2)]
    x, y = int(positions[0][0]), int(positions[0][1])
    # 在当前位置点击鼠标左键
    pyautogui.click(x, y)
    print(f"已在({x}, {y})位置点击")
    # 等待下次点击
    time.sleep(1000)
