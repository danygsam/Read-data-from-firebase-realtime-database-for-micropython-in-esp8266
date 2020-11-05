def wlan_connect(ssid, password):
    import network
    wlan = network.WLAN(network.STA_IF)
    if not wlan.active() or not wlan.isconnected():
        wlan.active(True)
        print('connecting to:', ssid)
        wlan.connect(ssid, password)
        while not wlan.isconnected():
            pass
    if wlan.isconnected():
        print('succesfully connected to', ssid)
    else:
        print('connection to', ssid, 'failed')
    print('network config:', wlan.ifconfig())
