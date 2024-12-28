import pyautogui
import time
from pynput.mouse import Listener

from pynput import mouse

def click_position():
    def on_click(x, y, button, pressed):
        nonlocal click_positions
        if button == mouse.Button.left and pressed:
            print(f"Left mouse button clicked at ({x}, {y})")
            click_positions.append((x, y))
        elif button == mouse.Button.right and pressed:
            print("Right mouse button clicked. Exiting...")
            listener.stop()

    listener = mouse.Listener(on_click=on_click)
    click_positions = []  # 存储鼠标点击位置的列表
    listener.start()
    print("Click the left mouse button to get the mouse position. Click the right mouse button to exit.")
    listener.join()
    return click_positions

if __name__ == '__main__':
    click_positions = click_position()
    print(click_positions)



