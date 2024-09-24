from pyautogui import *
import pyautogui
import pydirectinput
import time
import keyboard
import random
import win32api, win32con
import time
from ahk import *

ahk = AHK()

x = 0
y = 0
w = 0
z = 0

def click(x2,y2):
    win32api.SetCursorPos((x2,y2))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
while keyboard.is_pressed('p') == False:
    d = pyautogui.locateOnScreen('Bow.png', confidence=0.65)
    while keyboard.is_pressed('p') == False:
        if d == None:
            break
        if pyautogui.locateOnScreen('Bow.png', confidence=0.65) == None:
            break
        x = d[0]
        y = d[1]
        ahk.mouse_move(x = x,y = y , speed = 5, blocking = True)
        print("I can See it")
        time.sleep(0.5)
        break
    else:
        print("I am unable to see it")
        time.sleep(0.5)
