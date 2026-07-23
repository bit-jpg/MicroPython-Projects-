from machine import I2C, Pin
import sh1106, network, time


w = 128
h = 64
wifi = network.WLAN(network.WLAN.IF_STA)
led = Pin(2, Pin.OUT)
i2c = I2C(0, scl=Pin(22),sda=Pin(21) , freq=1_000_000)
#i2c_audio = I2C(1, scl=Pin(18),sda=Pin(19) , freq=400_000)

splash_text = "Hello"

# This also clears the display every boot
try:
    oled = sh1106.SH1106_I2C(w, h,i2c, None, 0x3c, rotate=0, delay=0)
    print(oled)
except OSError as error:
    print(f"Device not connected! {error}")