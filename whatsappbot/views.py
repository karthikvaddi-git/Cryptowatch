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
from .models import *
@csrf_exempt
def bot(request):
    if request.method=='GET':
        return HttpResponse("helo in bot view")

    if request.method=='POST':
        client = Client("AC1ac2e6dd551790ba9dcd1d3464eab564", "1722757f5c8f5842bf9e53b88b298f25")

        print(request.POST)
        message = request.POST['Body']
        sender_name = request.POST['ProfileName']
        sender_number = request.POST['From']
        print(message)

        if message == "1" :

            url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=INR&order=market_cap_desc&per_page=100&page=1&sparkline=false'
            data = requests.get(url).json()
            messagetosend = " "
            i=0;
            while i < 10:
                item=data[i]
                messagetosend = messagetosend + str(item['name']) + '\t' + str(item['current_price']) + '\n'
                i += 1
            """
            for item in data:
                messagetosend=messagetosend + str(item['name']) + '\t' +str(item['current_price']) + '\n'
            """

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

            url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=INR&order=market_cap_desc&per_page=100&page=1&sparkline=false'
            data = requests.get(url).json()
            string1="https://cointelegraph.com/"
            string2="https://www.coindesk.com/"
            string3="https://time.com/nextadvisor/investing/cryptocurrency/latest-crypto-news/"
            string4="https://cryptonews.com/"
            messagetosend = string1  + '\n' + string2 + '\n' + string3  + '\n'+ string4


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


        if message == "3":

            url='https://api.coingecko.com/api/v3/asset_platforms'
            data = requests.get(url).json()
            messagetosend=" "

            for item in data:
                messagetosend=messagetosend + str(item['name']) + '\n'




            try:

                msd = client.messages.create(
                    from_='whatsapp:+14155238886',
                    body=messagetosend,

                    to=sender_number
                )





            except TwilioRestException as e:
                print(e)
        if message == "4":

            url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=INR&order=market_cap_desc&per_page=100&page=1&sparkline=false'
            data = requests.get(url).json()
            string1="coinswitch"
            string2="coindx"
            string3="binance"
            string4="Ftx"
            messagetosend = string1  + '\n' + string2 + '\n' + string3  + '\n'+ string4


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

        if message == "5":


            string1 = "https://airdrops.io/"
            string2 = "https://www.binance.com/en/deposit-airdrop"
            string3 = "https://icomarks.com/airdrops"
            string4 = "https://airdropalert.com/"
            messagetosend = string1 + '\n' + string2 + '\n' + string3 + '\n' + string4

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

            messagetosent= "hello "+sender_name

            temp=    """ this is your crypto watch bot provides you all crypto market information
             1.Top 10 crypto market cap coins
             2.Best websites to follow cryptonews
             3. Blockchain asset platforms
             4.Best crypto trading platforms
             5.Airdrop websites 
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




