import pyautogui
import time
from basic import Basic
bs = Basic


class Nomads:

    def nomadtrain():
        NomadAttacks.nomadpresetattack(1280, 310) # Nomad 1 # 10 seconds
        time.sleep(2)
        NomadAttacks.nomadpresetattack(1480, 310) # Nomad 2 # 22 Seconds
        time.sleep(2)
        NomadAttacks.nomadpresetattack(1285, 600) # Nomad 3 # 34 Seconds
        time.sleep(2)
        NomadAttacks.nomadpresetattack(1380, 695) # Nomad 4 # 46 Seconds
        time.sleep(2)                                       # 48 Seconds
        
        time.sleep(240) # Attacks have how all finished
        
        rewardsvisible = 0
        while rewardsvisible < 1:            
            try: # Check if the rewards screen shows up
                x, y = pyautogui.locateCenterOnScreen('images/General/tick.png', grayscale=False) 
                pyautogui.moveTo(x, y, .2, pyautogui.easeInQuad)
                pyautogui.click()  
                rewardsvisible = 0   
                print('Accepting Rewards!')
                time.sleep(.2)   
                continue
            except TypeError: #if cant find image of the tick, continue on
                rewardsvisible = 1
        
        
        #reset nomad camps
        NomadAttacks.nomadtimereset(1280, 310) # Nomad Reset 1
        time.sleep(2)
        NomadAttacks.nomadtimereset(1480, 310) # Nomad Reset 2
        time.sleep(2)
        NomadAttacks.nomadtimereset(1285, 600) # Nomad Reset 3
        time.sleep(2)
        NomadAttacks.nomadtimereset(1380, 695) # Nomad Reset 4
        time.sleep(2)
        
class NomadAttacks:

    def nomadpresetattack(nomadx, nomaxy): #action takes 10 seconds total
        mousedelay = .2
        
        pyautogui.moveTo(nomadx, nomaxy, mousedelay, pyautogui.easeInQuad)
        pyautogui.click() 
        bs.clickon('images/General/attack.png', .45, mousedelay)
        bs.clickon('images/General/tick.png', .8, mousedelay)
        time.sleep(2)       
        pyautogui.moveTo(628, 938, mousedelay, pyautogui.easeInQuad) #open presets
        pyautogui.click()
        pyautogui.moveTo(521, 825, mousedelay, pyautogui.easeInQuad) #select all wave preset
        pyautogui.click()  
        pyautogui.moveTo(761, 936, mousedelay, pyautogui.easeInQuad) #select all waves
        pyautogui.click()
        pyautogui.moveTo(628, 938, mousedelay, pyautogui.easeInQuad) #open presets
        pyautogui.click()         
        pyautogui.moveTo(521, 847, mousedelay, pyautogui.easeInQuad) #select mantlets wave preset
        pyautogui.click()     
        pyautogui.moveTo(716, 936, mousedelay, pyautogui.easeInQuad) #select single wave
        pyautogui.click()
        
        
        bs.clickon('images/General/confirmattack.png', .8, mousedelay)        
        time.sleep(.2)        
        bs.clickon('images/General/horse1.png', .8, mousedelay)       
        bs.clickon('images/General/tick.png', .8, mousedelay)
        time.sleep(.7)
        
    def nomadtimereset(nomadx, nomady):
        mousedelay = .2
        pyautogui.moveTo(nomadx, nomady, mousedelay, pyautogui.easeInQuad)
        pyautogui.click() 
        bs.clickon('images/General/attack.png', .45, mousedelay)
        pyautogui.moveTo(1107, 544, mousedelay, pyautogui.easeInQuad) # skip time
        pyautogui.click()
        pyautogui.moveTo(893, 581, mousedelay, pyautogui.easeInQuad) # skip 30m
        pyautogui.click()
        time.sleep(.4)
        pyautogui.click()
        pyautogui.moveTo(855, 700, mousedelay, pyautogui.easeInQuad) # close menu
        pyautogui.click()
        time.sleep(.1)