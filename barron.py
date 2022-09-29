from lib2to3.pytree import type_repr
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
        bs.clickon('images/General/attack.png', .45, mousedelay)        
        bs.clickon('images/General/tick.png', .8, mousedelay)       
        time.sleep(2)       
        bs.clickon('images/General/autofillall.png', .8, mousedelay)       
        bs.clickon('images/General/confirmattack.png', .8, mousedelay)        
        time.sleep(.2)        
        bs.clickon('images/General/horse1.png', .8, mousedelay)       
        bs.clickon('images/General/tick.png', .8, mousedelay)
        
        time.sleep(.5)
        
    def attackadvanced(level):
                
        mousedelay = .2
        gl.click_button('Travel Overview')
        commanderremaining = 0
        
        while commanderremaining < 1:            
            try: # Check if commanders are still avaliable to send out
                x, y = pyautogui.locateCenterOnScreen('images/General/nocommanders.png', grayscale=False)  
                commanderremaining = 0   
                print('No Commanders Remaining')
                time.sleep(60)   
                continue
            except TypeError: #if cant find image of no commanders then procede with normal script
                commanderremaining = 1
                print('Commanders Remaining')
                bs.clickon('images/General/Exit Travel Overview.png', .8, mousedelay)
                time.sleep(.5)      
                    
                x, y = pyautogui.locateCenterOnScreen('images/robber%d.png' % (level), grayscale=False, confidence=.95, ) #region=(200, 150, 1400, 373)
                pyautogui.moveTo(x, y, mousedelay, pyautogui.easeInQuad)
                pyautogui.click()    
                    
                bs.clickon('images/General/attack.png', .45, mousedelay)
                bs.clickon('images/General/tick.png', .8, mousedelay)            
                time.sleep(2)           
                bs.clickon('images/General/autofillall.png', .8, mousedelay)
                bs.clickon('images/General/confirmattack.png', .8, mousedelay)            
                time.sleep(.2)            
                bs.clickon('images/General/horse1.png', .8, mousedelay)
                bs.clickon('images/General/tick.png', .8, mousedelay)            
                time.sleep(.5)

