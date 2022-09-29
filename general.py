import pyautogui
import time
import cv2
import os


from basic import Basic
bs = Basic

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
                bs.clickon('images/General/click_button/next.png', .9, .2)
                continue
            i = 1
        
        #Select Quantity
        bs.clickon('images/General/troops/Buttons/Quantity_Selector.png', .7, .2)
        pyautogui.typewrite(quantity, .2)
        bs.clickon('images/General/troops/Buttons/Recruit.png', .8, .2)

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
                bs.clickon('images/General/click_button/next.png', .9, .2)      
                continue
            i = 1
        
        #Select Quantity
        bs.clickon('images/General/troops/Buttons/Quantity_Selector.png', .7, .2) 
        pyautogui.typewrite(quantity, .2)
        bs.clickon('images/General/tools/Buttons/Produce.png', .8, .2)
        
    def travel(location):
        x, y = pyautogui.locateCenterOnScreen('images/General/click_button/%s/%s.png' % (location, location), grayscale=False)
        pyautogui.moveTo(x, y, .2, pyautogui.easeInQuad)
        pyautogui.click()
        
        x, y = pyautogui.locateCenterOnScreen('images/General/click_button/%s/travel.png' % (location), grayscale=False)
        pyautogui.moveTo(x, y, .2, pyautogui.easeInQuad)
        pyautogui.click()