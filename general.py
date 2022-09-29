import pyautogui
import time
import cv2
import os


os.chdir(os.path.dirname(os.path.abspath(__file__)))

class General:
    
    
    def click_button(button):
        try:
            x, y = pyautogui.locateCenterOnScreen('images/General/click_button/%s.png' % (button), grayscale=False)
            pyautogui.moveTo(x, y, .2, pyautogui.easeInQuad)
            pyautogui.click()
            time.sleep(2)
        except TypeError:
            print("Already at %s!" % (button))

    #Recruit Requires the recruitment screen to already be open
    def recruit(troop, quantity):
        #Select Troop
        i = 0
        while i == 0:        
            try:
                x, y = pyautogui.locateCenterOnScreen('images/General/troops/%s.png' % (troop), grayscale=False, confidence = .8)
                pyautogui.moveTo(x, y, .2, pyautogui.easeInQuad)
                pyautogui.click()
            except TypeError:
                x, y = pyautogui.locateCenterOnScreen('images/General/click_button/next.png', grayscale=False, confidence = .9)
                pyautogui.moveTo(x, y, .2, pyautogui.easeInQuad)
                pyautogui.click()
                continue
            i = 1
        
        #Select Quantity
        x, y = pyautogui.locateCenterOnScreen('images/General/troops/Buttons/Quantity_Selector.png', grayscale=False, confidence = .7)
        pyautogui.moveTo(x, y, .2, pyautogui.easeInQuad)
        pyautogui.click()
        pyautogui.typewrite(quantity, .2)
        x, y = pyautogui.locateCenterOnScreen('images/General/troops/Buttons/Recruit.png', grayscale=False, confidence = .8)
        pyautogui.moveTo(x, y, .2, pyautogui.easeInQuad)
        pyautogui.click()

    #Produce Requires the recruitment screen to already be open
    def produce(tool, quantity):
        #Select Tool
        i = 0
        while i == 0:        
            try:
                x, y = pyautogui.locateCenterOnScreen('images/General/tools/%s.png' % (tool), grayscale=False, confidence = .8)
                pyautogui.moveTo(x, y, .2, pyautogui.easeInQuad)
                pyautogui.click()
            except TypeError:
                x, y = pyautogui.locateCenterOnScreen('images/General/click_button/next.png', grayscale=False, confidence = .9)
                pyautogui.moveTo(x, y, .2, pyautogui.easeInQuad)
                pyautogui.click()
                continue
            i = 1
        
        #Select Quantity
        x, y = pyautogui.locateCenterOnScreen('images/General/troops/Buttons/Quantity_Selector.png', grayscale=False, confidence = .7)
        pyautogui.moveTo(x, y, .2, pyautogui.easeInQuad)
        pyautogui.click()
        pyautogui.typewrite(quantity, .2)
        x, y = pyautogui.locateCenterOnScreen('images/General/tools/Buttons/Produce.png', grayscale=False, confidence = .8)
        pyautogui.moveTo(x, y, .2, pyautogui.easeInQuad)
        pyautogui.click()
        
    def travel(location):
        x, y = pyautogui.locateCenterOnScreen('images/General/click_button/%s/%s.png' % (location, location), grayscale=False)
        pyautogui.moveTo(x, y, .2, pyautogui.easeInQuad)
        pyautogui.click()
        
        x, y = pyautogui.locateCenterOnScreen('images/General/click_button/%s/travel.png' % (location), grayscale=False)
        pyautogui.moveTo(x, y, .2, pyautogui.easeInQuad)
        pyautogui.click()