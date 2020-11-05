import time
from machine import Pin

Firebaseurl = "https://your_PROJECT_URL/mains.json"

led = Pin(16, Pin.OUT)

# Reading JSON
def readData():
    import urequests as ureq
    req = ureq.get(Firebaseurl)
    return req.json()

# Reading Data
def activate():
    while True:
        data = readData()
        print(data['output_16'])
        led.value(data['output_16'])
        time.sleep(5)
