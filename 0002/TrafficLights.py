from gpiozero import LED
from time import sleep

green = LED(17)
yellow = LED(27)
red = LED(22)
time = 1

count = 1
while count <= 5:
    print('---Loop:', count)
    
    print('GREEN ON - YELLOW OFF - RED OFF')
    green.on()
    yellow.off()
    red.off()    
    sleep(time)   
    
    print('GREEN OFF - YELLOW ON - RED OFF')
    green.off()
    yellow.on()
    red.off()    
    sleep(time) 
    
    print('GREEN OFF - YELLOW OFF - RED ON')
    green.off()
    yellow.off()
    red.on()    
    sleep(time)
    
    count = count + 1

green.off()
yellow.off()
red.off() 