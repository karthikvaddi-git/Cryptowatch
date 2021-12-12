from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from .models import Cointracker,Cryptodata,Phonenumber
from decouple import config
from twilio.rest import Client
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def register(request):
    if request.method=='GET':


        #    account_sid = "AC1ac2e6dd551790ba9dcd1d3464eab564"
       #     auth_token = "a6a841cf8bb50923b9d5259a83e01e8e"
      #      client = Client(account_sid, auth_token)

        #    notification = client.notify.services("IS9c85d2b8056f1b8da34c582cc2408815").notifications.create(
         #       to_binding='{"binding_type":"sms", "address":"+917396450288"}',
          #      body='check twillio service notify')
            return render(request, "cointrack.html")


    if request.method=='POST':
        print(request.POST)
        username = request.POST.get('username',False)
        print("the username is ")
        print(username)

        """"username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        user = User.objects.create_user(username=username, email=username, password=password)
        user.save()"""

        return HttpResponse("registered succesfully")


def logintoweb(request):

    if request.method=='POST':

        username=request.POST['username']
        password=request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('cointrack')

        else:
            return HttpResponse("your username or password is wrong")


@login_required
def cointrack(request):
    if request.method=="GET":
        return render(request,'cointrack.html')
    if request.method=="POST":
        print(request)
        print("the data is")
        print(request.POST)
        coinname=request.POST['coiname']
        coinprice=request.POST['coinprice']
        coinstatus=request.POST['fav_language']
        if coinstatus=="coinfall":
            coinobj = Cointracker(user=request.user, name=coinname, triggerprice=coinprice, pricerises=False)
            coinobj.save()

        else:
            coinobj = Cointracker(user=request.user, name=coinname, triggerprice=coinprice)
            coinobj.save()
        return HttpResponse(request.POST)
























