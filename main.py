from machine import Pin
from time import sleep
import sys
from connection import wlan_connect
from firebase import activate

# ESP8266 BuiltIn LED
led = Pin(16, Pin.OUT)

print('\n\nStarted...')

# Type your WIFI SSID (name)
ssid = input('Enter SSID : ')

# Type your WIFI password
password = input('Enter PASSWORD : ')

for i in range(1):
    wlan_connect(ssid, password)

# For Testing LED
for _ in range(5):
    led.value(0)
    sleep(1)
    led.value(1)
    sleep(1)

# To Read data from firebase
activate()