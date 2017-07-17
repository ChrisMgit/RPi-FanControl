import time
import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)
gpio.setup(18, gpio.OUT)
print("This won't work without a data lead!")

while True:
    with open('/sys/class/thermal/thermal_zone0/temp') as temp:
        tempC = float(temp.read())/1000
        cpu_temp = ("%.2f" % tempC)
        if cpu_temp > 40:
            gpio.output(18, gpio.HIGH)
        else:
            gpio.output(18, gpio.LOW)
            
            
