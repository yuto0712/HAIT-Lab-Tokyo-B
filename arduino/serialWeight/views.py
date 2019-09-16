from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
import serial
import re

class SignalTemplateView(TemplateView):
    template_name = "signal.html"
    ser = serial.Serial("/dev/cu.usbmodem14201", 9600, timeout=None)

    while True:
        line = ser.readline()
        print(line)

    ser.close()

    def post(self, request):
        if request.method == "POST":
            if "LED" in request.POST:
                ser = serial.Serial("/dev/cu.usbmodem14101")
                ser.write(1)
                ser.close()
        return render(request, self.template_name)


