import pyautogui
import time
import cv2
import os
import pytesseract

from general import General


os.chdir(os.path.dirname(os.path.abspath(__file__)))

gl = General

class AutoBarron:
        
    def attackbasic(level):
        
        mousedelay = .2
                
        x, y = pyautogui.locateCenterOnScreen('images/robber%d.png' % (level), grayscale=False, confidence=.95)
        pyautogui.moveTo(x, y, mousedelay, pyautogui.easeInQuad)
        pyautogui.click()
        
        x, y = pyautogui.locateCenterOnScreen('images/attack.png', grayscale=False, confidence=.45)
        pyautogui.moveTo(x, y, mousedelay, pyautogui.easeInQuad)
        pyautogui.click()
        
        x, y = pyautogui.locateCenterOnScreen('images/tick.png', grayscale=False, confidence=.8)
        pyautogui.moveTo(x, y, mousedelay, pyautogui.easeInQuad)
        pyautogui.click()
        
        time.sleep(2)
        
        x, y = pyautogui.locateCenterOnScreen('images/autofillall.png', grayscale=False, confidence=.8)
        pyautogui.moveTo(x, y, mousedelay, pyautogui.easeInQuad)
        pyautogui.click()
        
        x, y = pyautogui.locateCenterOnScreen('images/confirmattack.png', grayscale=False, confidence=.8)
        pyautogui.moveTo(x, y, mousedelay, pyautogui.easeInQuad)
        pyautogui.click()
        
        time.sleep(.2)
        x, y = pyautogui.locateCenterOnScreen('images/horse1.png', grayscale=False, confidence=.8)
        pyautogui.moveTo(x, y, mousedelay, pyautogui.easeInQuad)
        pyautogui.click()
        
        x, y = pyautogui.locateCenterOnScreen('images/tick.png', grayscale=False, confidence=.8)
        pyautogui.moveTo(x, y, mousedelay, pyautogui.easeInQuad)
        pyautogui.click()
        
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
            x, y = pyautogui.locateCenterOnScreen('images/Exit Travel Overview.png', grayscale=False)
            pyautogui.moveTo(x, y, .2, pyautogui.easeInQuad)
            pyautogui.click()
            time.sleep(.5)
            
            
            x, y = pyautogui.locateCenterOnScreen('images/robber%d.png' % (level), grayscale=False, confidence=.90, region=(200, 150, 1400, 373))
            pyautogui.moveTo(x, y, mousedelay, pyautogui.easeInQuad)
            pyautogui.click()
            
            x, y = pyautogui.locateCenterOnScreen('images/attack.png', grayscale=False, confidence=.45)
            pyautogui.moveTo(x, y, mousedelay, pyautogui.easeInQuad)
            pyautogui.click()
            
            x, y = pyautogui.locateCenterOnScreen('images/tick.png', grayscale=False, confidence=.8)
            pyautogui.moveTo(x, y, mousedelay, pyautogui.easeInQuad)
            pyautogui.click()
            
            time.sleep(2)
            
            x, y = pyautogui.locateCenterOnScreen('images/autofillall.png', grayscale=False, confidence=.8)
            pyautogui.moveTo(x, y, mousedelay, pyautogui.easeInQuad)
            pyautogui.click()
            
            x, y = pyautogui.locateCenterOnScreen('images/confirmattack.png', grayscale=False, confidence=.8)
            pyautogui.moveTo(x, y, mousedelay, pyautogui.easeInQuad)
            pyautogui.click()
            
            time.sleep(.2)
            x, y = pyautogui.locateCenterOnScreen('images/horse1.png', grayscale=False, confidence=.8)
            pyautogui.moveTo(x, y, mousedelay, pyautogui.easeInQuad)
            pyautogui.click()
            
            x, y = pyautogui.locateCenterOnScreen('images/tick.png', grayscale=False, confidence=.8)
            pyautogui.moveTo(x, y, mousedelay, pyautogui.easeInQuad)
            pyautogui.click()
            
            time.sleep(.5)