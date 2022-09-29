#imports
import os
import time

#not sure if i need this
os.chdir(os.path.dirname(os.path.abspath(__file__)))

#other files
from basic import Basic
from general import General
from barron import AutoBarron
from scraper import Scraper

#type definitions
bs = Basic
gl = General
barronfarm = AutoBarron
scrape = Scraper



i = 0
while i < 1:
    barronfarm.attackadvanced(1)

#gl.recruit('Veteran Heavy Crossbowman', '2')