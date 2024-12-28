from Tool import click_position_record
from Tool import auto_click
from Tool import locate_image
import Click_position_obtain
import AutoClick
import pyautogui
import time
from pynput import mouse


def jiemianpanduan():
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

def position_cal(location):

    position = (location[0] + location[3] / 2, location[1] + location[2] / 2)
    x, y = int(position[0]), int(position[1])
    return x, y

def auto_click_help():
    def on_click(x, y, button, pressed):
        nonlocal flag
        if button == mouse.Button.right and pressed:
            print("Right mouse button clicked. Exiting...")
            flag = 0
            listener.stop()

    location_lianmeng = locate_image(r'Figures\lianmeng.png', 0.80)
    try:
        x, y = position_cal(location_lianmeng)
        pyautogui.click(x, y)
        print(f"已在({x}, {y})位置点击")
    except:
        print('Find failed.')


    time.sleep(2)

    location_lianmenghuzhu = locate_image(r'Figures\lianmenghuzhu.png', 0.80)
    # print(location_lianmenghuzhu)
    try:
        x, y = position_cal(location_lianmenghuzhu)
        pyautogui.click(x, y)
        print(f"已在({x}, {y})位置点击")
    except:
        print('Find failed.')

    time.sleep(2)
    listener = mouse.Listener(on_click=on_click)
    x, y = position_cal(location_lianmenghuzhu)
    flag = 1
    listener.start()
    print("Click the right mouse button to exit.")


    print('hello')
    while flag:
        pyautogui.click(x - 25, y + 60)
        print(f"已在({x}, {y})位置点击")
        time.sleep(0.01)
    listener.join()
if __name__ == '__main__':
    auto_click_help()