from django.shortcuts import render
from django.views.generic import TemplateView
import serial
import slackweb

class SignalTemplateView(TemplateView):
    template_name = "signal.html"


    def get(self, request):
        ser = serial.Serial("/dev/cu.usbmodem14201", 9600, timeout=None)

        if request.method == "GET":
            output = ser.readline().decode("utf-8").strip("\r\n")
            if output == "H":
                params = {
                    "status": "danger"
                }
                send_slack_message()
            else:
                params = {
                    "status": "safe"
                }
            print(output)

        return render(request, "signal.html", params)

def send_slack_message():
    slack = slackweb.Slack(url="https://hooks.slack.com/services/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")
    slack.notify(text="残量が足りません！補給したほうがいいよ．")






