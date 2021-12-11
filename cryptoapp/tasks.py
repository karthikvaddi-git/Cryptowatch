from django.contrib.auth import get_user_model
from cryptowatch import settings
from celery import shared_task
from celery import shared_task
from .models import  Cryptodata
import json
#from .utils import get_random_code
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
#from celery.decorators import periodic_task
#from celery.task.schedules import crontab
import requests
from django.core import serializers


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

