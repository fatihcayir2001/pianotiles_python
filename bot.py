'''
AUTO PIANO TILES (by luna lol)

varibles:

delay - the delay between clicks
black - the rgb code for the black box

requirements:

pyautogui
pywin32
pillow

thease will automaticly be installed at start
'''

''''
Bot works on that website https://www.agame.com/game/magic-piano-tiles
you can run for another game but you might have to change the color "black" according to the buttons color


'''





import os

e = ["pyautogui", "pywin32", "pillow"]

for x in e:
    os.system(f"pip install {x}")

import pyautogui, time, ctypes, threading, win32api, keyboard, win32con
from PIL import ImageGrab
from tkinter import *



delay = 0.04 # CHANGE THIS TO YOUR LIKEING -  i suggest a delay speed of about 0.02 to 0.04


black = (0, 0, 0) # DO NOT change this unless you dm me asking what it does

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.02) #This pauses the script for 0.01 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)




places = {} # a dict to store x and y data

def mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)

def app():
    mbox("Piano Tiles Bot", "After clicking ok you will have 3 seconds to get ready. Hold Q anytime to stop", 0)
    time.sleep(3)
    threading.Thread(target=appthread).start()

def appthread():
    while keyboard.is_pressed('q') == False:
        px = ImageGrab.grab().load()
        for y in range(0, 100, 10):
            for x in range(0, 100, 10):
                v1 = px[places["1"]["1"], places["1"]["2"]]
                v2 = px[places["2"]["1"], places["2"]["2"]]
                v3 = px[places["3"]["1"], places["3"]["2"]]
                v4 = px[places["4"]["1"], places["4"]["2"]]
        if v1 == black:
            click(places["1"]["1"], places["1"]["2"])

        if v2 == black:
            click(places["2"]["1"], places["2"]["2"])

        if v3 == black:
            click(places["3"]["1"], places["3"]["2"])

        if v4 == black:
            click(places["4"]["1"], places["4"]["2"])



def select1():
    mbox("Piano Tiles Bot", "After clicking ok please press G when your mouse is over row one!", 0)
    while keyboard.is_pressed('g') == False:
        x, y = win32api.GetCursorPos()
    places["1"] = {}
    places["1"]["1"] = x
    places["1"]["2"] = y

def select2():
    mbox("Piano Tiles Bot", "After clicking ok please press G when your mouse is over row two!", 0)
    while keyboard.is_pressed('g') == False:
        x, y = win32api.GetCursorPos()
    places["2"] = {}
    places["2"]["1"] = x
    places["2"]["2"] = y

def select3():
    mbox("Piano Tiles Bot", "After clicking ok please press G when your mouse is over row three!", 0)
    while keyboard.is_pressed('g') == False:
        x, y = win32api.GetCursorPos()
    places["3"] = {}
    places["3"]["1"] = x
    places["3"]["2"] = y

def select4():
    mbox("Piano Tiles Bot", "After clicking ok please press G when your mouse is over row four!", 0)
    while keyboard.is_pressed('g') == False:
        x, y = win32api.GetCursorPos()
    places["4"] = {}
    places["4"]["1"] = x
    places["4"]["2"] = y

root = Tk()
root.title("Piano Tiles Bot")
root.geometry("200x200")

Button(root, text="Select Row 1", command=select1).pack()
Button(root, text="Select Row 2", command=select2).pack()
Button(root, text="Select Row 3", command=select3).pack()
Button(root, text="Select Row 4", command=select4).pack()
Button(root, text="Start", command=app).pack()
root.mainloop()
