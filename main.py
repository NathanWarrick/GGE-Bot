import os
import time
import pyautogui
import pytesseract

#other files
from barron import AutoBarron
from general import General
from scraper import Scraper

#not sure if i need this
os.chdir(os.path.dirname(os.path.abspath(__file__)))

barronfarm = AutoBarron
gl = General
scrape = Scraper



i = 0
while i < 1:
    barronfarm.attackadvanced(1)