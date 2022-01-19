import network
import time

#We set up a station by decalaring a variable named wlan and calling the WLAN function from the netwrok library file. We select the mode WLAN.STA which is nothing by WiFi Station that is
#a mode where a device joins a network that already exists like how a smartphone does.

wlan = network.WLAN(mode=network.WLAN.STA)

#We now have to connect to the WiFi using the WiFi name that is the SSID and the password. WLAN.WPA2 is the Wi-Fi Protected Access II security which is the password of the WiFi Network.
wlan.connect('UserHotSpot', auth=(network.WLAN.WPA2, 'test_pycom'))

#In case the WiFi is not able to connect, the device is asked to sleep for a duration of 50ms.
while not wlan.isconnected():
    time.sleep_ms(50)

#In case the WiFi connection is successful, we want the device to print its IP Configuration.
print(wlan.ifconfig())
#The output shall be of this template: # (ip, subnet_mask, gateway, DNS_server)

#Make sure the WiFi SSID (WiFi/Hotspot name) and Password is typed exactly the same as they are case-sensitive.  
