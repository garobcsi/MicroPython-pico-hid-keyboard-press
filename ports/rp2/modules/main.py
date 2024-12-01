import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from machine import Pin

# Initialize the keyboard
kbd = Keyboard(usb_hid.devices)

# Initialize the onboard LED
led = Pin(25, Pin.OUT)

while True:
    # Turn on the LED
    led.value(1)

    # Press and release the 'G' key
    kbd.press(Keycode.G)
    kbd.release_all()  # Releases all pressed keys
    print("Pressed G")

    # Wait briefly to show LED
    time.sleep(0.5)  # LED on for 0.5 seconds

    # Turn off the LED
    led.value(0)

    # Wait 9.5 seconds (total cycle = 10 seconds)
    time.sleep(9.5)
