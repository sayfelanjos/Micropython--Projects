from pyb import LED
from pyb import delay

led = LED(1)

while True:
    led.on()
    delay(1000)
    led.off()
    delay(1000)


