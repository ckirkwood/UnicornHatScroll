from UHScroll import *
from time import sleep
import os 

# Return CPU temperature as a character string                                      
def getCPUtemperature():
    res = os.popen('vcgencmd measure_temp').readline()
    return(res.replace("temp=","").replace("'C\n",""))

temp = getCPUtemperature()

unicorn_scroll(temp + '~degrsc','yellow',200,0.1)

