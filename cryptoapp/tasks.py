from cryptowatch import settings
from celery import shared_task
from .models import  Cryptodata,Cointracker,Phonenumber
import json
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
import requests
from django.core import serializers
from twilio.rest import Client
from decouple import config


@shared_task
def get_crypto_data():
    url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=INR&order=market_cap_desc&per_page=100&page=1&sparkline=false'
    data = requests.get(url).json()


    for item in data:
        p, _ = Cryptodata.objects.get_or_create(name=item['name'])
        p.image = item['image']
        p.price = item['current_price']
        p.rank = item['market_cap_rank']
        p.market_cap = item['market_cap']
        p.save()



# Task to send coin price alert to user

@shared_task
def trackcoinprice():
    client = Client("AC1ac2e6dd551790ba9dcd1d3464eab564", "1722757f5c8f5842bf9e53b88b298f25")
    pricerisesobjects = Cointracker.objects.filter(messagesent=False)
    #   print(pricerisesobjects.triggerprice)

    print(pricerisesobjects)
    for item in pricerisesobjects:
        triggerprice = item.triggerprice
        coinname = item.name
        try:
            coinobject = Cryptodata.objects.get(name=coinname)
        except Cryptodata.DoesNotExist:
            user = None

        phoneobj = Phonenumber.objects.get(user=item.user)
        phonenumber = phoneobj.phone_number
        coinprice = coinobject.price
        if triggerprice >= coinprice:

            # twillio sending message


            messagetext = "Your price rise alert for " + coinname


            message = client.messages.create(from_="+12184801731", body=messagetext, to=phonenumber)
            if message.sid:
                Cointracker.objects.filter(user=item.user).filter( name=item.name).filter( pricerises=True) .update(messagesent=True)
            else:

                print("message was not sent ")



        if triggerprice <= coinprice:
            # account_sid = accounts_sid
            # auth_token = auths_token


            messagetext = "Your price drop alert for " + coinname

            message = client.messages.create(from_="+12184801731", body=messagetext, to=phonenumber)
            if message.sid:
                Cointracker.objects.filter(user=item.user).filter(name=item.name).filter(pricerises=False).update(
                    messagesent=True)


            else:

                print("message was not sent")















