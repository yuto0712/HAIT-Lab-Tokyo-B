import serial
import re

ser = serial.Serial("/dev/cu.usbmodem14201", 9600, timeout=None)
'''
while True:
    line = ser.readline()
    print(line)
'''
while True:
    output = ser.readline().decode("utf-8").strip("\r\n")
    print(type(output))
    if output == "H":
        print("high!!!")
        break;
    else:
        print(output)
ser.close()
