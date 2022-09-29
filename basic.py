import pyautogui
import time
import cv2 as cv

class Basic:
    
    def clickon(path, confidencevalue, speed):
            x, y = pyautogui.locateCenterOnScreen(path, confidence = confidencevalue)
            pyautogui.moveTo(x, y, speed, pyautogui.easeInQuad)
            pyautogui.click()