from django.shortcuts import render
import twilio
from twilio.base.exceptions import TwilioRestException
# Create your views here.
from django.shortcuts import render,HttpResponse
from django.contrib.auth.models import User
import twilio.rest
from decouple import config
from twilio.rest import Client
from django.views.decorators.csrf import csrf_exempt,csrf_protect
import json
@csrf_exempt
def bot(request):
    if request.method=='GET':
        return HttpResponse("helo in bot view")

    if request.method=='POST':

        print(request.POST)
        message = request.POST['Body']
        sender_name = request.POST['ProfileName']
        sender_number = request.POST['From']
        if message == "hi":
            client = Client("AC1ac2e6dd551790ba9dcd1d3464eab564", "326d9c470a84843106f42f173d203101")

            try:

                msd = client.messages.create(
                    from_='whatsapp:+14155238886',
                    body='check 1 for market right now 2 for crypto news ',

                    to=sender_number
                )
                if msd.sid:
                    print("data was goog")



            except TwilioRestException as e:
                print(e)




        return HttpResponse("hello")




