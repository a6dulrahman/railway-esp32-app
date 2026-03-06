from machine import Pin
from time import sleep
from config import LED_RED, LED_YELLOW, LED_GREEN, TIME_RED, TIME_YELLOW, TIME_GREEN

# Setup LEDs
red = Pin(LED_RED, Pin.OUT)
yellow = Pin(LED_YELLOW, Pin.OUT)
green = Pin(LED_GREEN, Pin.OUT)

try:
    while True:
        red.value(1)
        yellow.value(0)
        green.value(0)
        sleep(TIME_RED)

        red.value(0)
        yellow.value(1)
        green.value(0)
        sleep(TIME_YELLOW)

        red.value(0)
        yellow.value(0)
        green.value(1)
        sleep(TIME_GREEN)

except KeyboardInterrupt:
    red.value(0)
    yellow.value(0)
    green.value(0)
    print("Semaphore stopped")