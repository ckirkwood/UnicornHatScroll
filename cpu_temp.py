from UHScroll import *
from time import sleep
import os 

def getCPUtemperature():
    res = os.popen('vcgencmd measure_temp').readline()
    return(res.replace("temp=","").replace("'C\n",""))

temp = getCPUtemperature()

unicorn_scroll('CPU-' + temp + '~degrsc','yellow',200,0.07)

