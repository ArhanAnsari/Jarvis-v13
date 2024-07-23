'''
Author: Avi Sinha (https://github.com/Avi0981)
'''

import pyautogui
import time

def whatsapp_call(contact_name):
    pyautogui.press('win')
    time.sleep(0.2)
    pyautogui.typewrite('whatsapp')
    time.sleep(0.2)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.click(1980, 10)
    time.sleep(0.2)
    pyautogui.moveTo(1000, 500)
    time.sleep(0.2)
    pyautogui.press('win')
    time.sleep(0.2)
    pyautogui.typewrite('whatsapp')
    time.sleep(0.2)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.typewrite(contact_name)
    time.sleep(0.2)
    pyautogui.press('tab')
    time.sleep(0.2)
    pyautogui.press('enter')
    for _ in range(5):
        pyautogui.press('tab')
        time.sleep(0.05)
    pyautogui.press('enter')
    

if __name__ == '__main__':
    whatsapp_call('Mom')
