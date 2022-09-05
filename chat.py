import pyautogui
import time
time.sleep(3)
count=0
while count<30:
    pyautogui.typewrite("Hey! You ")
    #pyautogui.typewrite("\n ")
    #pyautogui.typewrite("Idot")

    #time.sleep(10*2)
    pyautogui.press("enter")
    
    count+=1
    #time.sleep()
