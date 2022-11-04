from tkinter.font import BOLD
import pyautogui
import time
time.sleep(4)
count=0
while count<=100:
    pyautogui.typewrite("i love you")
    pyautogui.press("enter")
    count=count+1
