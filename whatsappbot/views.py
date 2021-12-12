from django.shortcuts import render
import twilio
import requests
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
        print(message)

        if message == "1" :
            client = Client("AC1ac2e6dd551790ba9dcd1d3464eab564", "326d9c470a84843106f42f173d203101")
            url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=INR&order=market_cap_desc&per_page=100&page=1&sparkline=false'
            data = requests.get(url).json()
            for item in data:
                messagetosend=" "
                messagetosend=messagetosend +str(item['name']) +"  "+str(item['current_price'])


            try:

                msd = client.messages.create(
                    from_='whatsapp:+14155238886',
                    body=messagetosend,

                    to=sender_number
                )
                if msd.sid:
                    print("in 1 block")




            except TwilioRestException as e:
                print(e)

        if message == "2":
            client = Client("AC1ac2e6dd551790ba9dcd1d3464eab564", "326d9c470a84843106f42f173d203101")
            url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=INR&order=market_cap_desc&per_page=100&page=1&sparkline=false'
            data = requests.get(url).json()
            string1="https://cointelegraph.com/"
            string2="https://www.coindesk.com/"
            string3="https://time.com/nextadvisor/investing/cryptocurrency/latest-crypto-news/"
            string4="https://cryptonews.com/"

            for item in data:
                messagetosend = " "
                messagetosend = string1  + string2 + string3  + string4


            try:

                msd = client.messages.create(
                    from_='whatsapp:+14155238886',
                    body=messagetosend,

                    to=sender_number
                )
                if msd.sid:
                    print("in 1 block")




            except TwilioRestException as e:
                print(e)

        if message == "hi" or message =="HI" or message == "Hi":
            client = Client("AC1ac2e6dd551790ba9dcd1d3464eab564", "326d9c470a84843106f42f173d203101")
            messagetosent= "hello "+sender_name
            temp=    """  this is your crypto watch bot provides you all crypto market information
             1.top profit
             2.top loss
             3.best defi
            """
            messagetosent=messagetosent + temp


            try:

                msd = client.messages.create(
                    from_='whatsapp:+14155238886',
                    body=messagetosent,

                    to=sender_number
                )
                if msd.sid:
                    print("data was goog")



            except TwilioRestException as e:
                print(e)
        return HttpResponse("hello")




