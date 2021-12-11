from django.shortcuts import render,HttpResponse
from django.contrib.auth.models import User
# Create your views here.
def register(request):
    if request.method=='GET':
        return render(request, "registration.html")
    if request.method=='POST':
        username=request.POST['email']
        email=request.POST['email']
        password=request.POST['psw']
        user = User.objects.create_user(username=username, email=username, password=password)
        user.save()
        return HttpResponse("regiered succesfully")












