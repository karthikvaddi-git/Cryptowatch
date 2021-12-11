from django.shortcuts import render,HttpResponse
from django.contrib.auth.models import User
from .models import Cointracker,Cryptodata,Phonenumber
from decouple import config
from twilio.rest import Client

# Create your views here.
def register(request):
    if request.method=='GET':

            account_sid = "AC1ac2e6dd551790ba9dcd1d3464eab564"
            auth_token = "a6a841cf8bb50923b9d5259a83e01e8e"
            client = Client(account_sid, auth_token)

            notification = client.notify.services("IS9c85d2b8056f1b8da34c582cc2408815").notifications.create(
                to_binding='{"binding_type":"sms", "address":"+917396450288"}',
                body='check twillio service notify')
            return render(request, "registration.html")
    if request.method=='POST':
        username=request.POST['email']
        email=request.POST['email']
        password=request.POST['psw']
        user = User.objects.create_user(username=username, email=username, password=password)
        user.save()
        return HttpResponse("regiered succesfully")












