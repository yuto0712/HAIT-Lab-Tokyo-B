import serial
import re

ser = serial.Serial("/dev/cu.usbmodem14101", 9600, timeout=None)

while True:
    line = ser.readline()
    print(line)

ser.close()
