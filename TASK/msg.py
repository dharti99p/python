import pyautogui as dm
import time
msg=input("enter the msg : ")
n=int(input("enter the msg count : "))
time.sleep(3)
for i in range(n):
    dm.typewrite(msg)
    dm.press("Enter")