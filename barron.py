import pyautogui
import time
import cv2
import os
import pytesseract

from general import General
from basic import Basic

os.chdir(os.path.dirname(os.path.abspath(__file__)))

gl = General
bs = Basic

class AutoBarron:
        
    def attackbasic(level):
        
        mousedelay = .2
                
        x, y = pyautogui.locateCenterOnScreen('images/robber%d.png' % (level), grayscale=False, confidence=.95)
        pyautogui.moveTo(x, y, mousedelay, pyautogui.easeInQuad)
        pyautogui.click()       
        bs.clickon('images/attack.png', .45, mousedelay)        
        bs.clickon('images/tick.png', .8, mousedelay)       
        time.sleep(2)       
        bs.clickon('images/autofillall.png', .8, mousedelay)       
        bs.clickon('images/confirmattack.png', .8, mousedelay)        
        time.sleep(.2)        
        bs.clickon('images/horse1.png', .8, mousedelay)       
        bs.clickon('images/tick.png', .8, mousedelay)
        
        time.sleep(.5)
        
    def attackadvanced(level):
                
        mousedelay = .2
        commandersremaining = 0
        gl.click_button('Travel Overview')
        
        commanders = pyautogui.screenshot('Images/temp/commanders.png', region=(1008, 438, 40, 17))
        commandersimg = commanders.convert('L')
        commandersremaining = pytesseract.image_to_string(commandersimg)
        commandersremaining = commandersremaining[:-5]
        print('Commanders Remaining %s' % (commandersremaining))
        
        while int(commandersremaining) < 1:
            time.sleep(60)
            commanders = pyautogui.screenshot('Images/temp/commanders.png', region=(1008, 438, 20, 15)) # Add More itterations of the image search to allow more tries with different settings
            #commandersimg = commanders.convert('L')
            commandersremaining = pytesseract.image_to_string(commanders)
            #commandersremaining = commandersremaining[:-5]
            print('Commanders Remaining %s' % (commandersremaining))
        else:
            bs.clickon('images/Exit Travel Overview.png', .9, mousedelay)
            time.sleep(.5)      
                  
            x, y = pyautogui.locateCenterOnScreen('images/robber%d.png' % (level), grayscale=False, confidence=.9, ) #region=(200, 150, 1400, 373)
            pyautogui.moveTo(x, y, mousedelay, pyautogui.easeInQuad)
            pyautogui.click()    
                   
            bs.clickon('images/attack.png', .45, mousedelay)
            bs.clickon('images/tick.png', .8, mousedelay)            
            time.sleep(2)           
            bs.clickon('images/autofillall.png', .8, mousedelay)
            bs.clickon('images/confirmattack.png', .8, mousedelay)            
            time.sleep(.2)            
            bs.clickon('images/horse1.png', .8, mousedelay)
            bs.clickon('images/tick.png', .8, mousedelay)            
            time.sleep(.5)