import pyautogui
import time

from mouseinfo import position
from pynput import keyboard

'''
auto_click(positions, interval=1):
    positions: a list of positions to be clicked
    interval: interval between clicks
'''

def auto_click(positions, interval=-1):
    if interval == -1:
        interval = [0.1] * len(positions)
    should_exit = False
    def on_press(key):
        nonlocal should_exit
        if key == keyboard.Key.f12:
            print("F12 key pressed. Exiting loop...")
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
        print("Stopped auto-clicking")
    except KeyboardInterrupt:
        print("Stopped auto-clicking")

if __name__ == '__main__':
    auto_click([(500,500), (200,300)], intervals=[1,1])