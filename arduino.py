import serial
import re

ser = serial.Serial("/dev/cu.usbmodem14101", 9600, timeout=None)

while True:
    line = ser.readline()
    if "High" in line:
        line = "High"
        
    print(line)

ser.close()
