from gpiozero import LED
from time import sleep

led = LED(18)

count = 0
while count < 10:
    print ('---Loop:', count)
    led.on()
    print ('Led ON')
    sleep(1)    
    led.off()
    print ('LED OFF')
    sleep(1)
    count = (count + 1)

led.off()