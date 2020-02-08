from RPi_I2C_driver import I2CDevice
from RPi_I2C_driver import lcd
import time

my_lcd = lcd()
# test 2
my_lcd.lcd_display_string("RPi I2C test", 1)
my_lcd.lcd_display_string(" Custom chars", 2)

time.sleep(2) # 2 sec delay

my_lcd.lcd_clear()
