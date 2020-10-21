from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import UserForm
from .models import Company, Employee, Nowcapture
from django.views import generic
from django.http import JsonResponse
from django.conf import settings
import datetime
import base64
import os

def signup(request):
    #계정 생성
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            userName = form.cleaned_data.get('username')
            Password = form.cleaned_data.get('password1')
            user = authenticate(username=userName, password=Password)
            login(request,user)
            return render(request,'delivery/login.html')
     
    else:
        form = UserForm()
    return render(request, 'delivery/signup.html', {'form': form})

def CapturePage(request):
    return render(request, 'face/CapturePage.html')

def DeliveryInformation(request):
    #현재 시간 불러옴
    now = datetime.datetime.now()
    #현재 년-월-일만 추출
    nowDate = now.strftime('%Y-%m-%d')
    
    #db에서 데이터 추출
    data = Nowcapture.objects.filter(todaydate = nowDate)

   # filename = 'testdecode.png'
    #face = Nowcapture.objects.filter(nowcapture = 'L03').filter(todaydate = nowDate)
    #face = face[22:]#'data:image/png;base64'부분을 제거
    
    #캡쳐사진 경로에 저장
    #path = str(os.path.join(settings.STATIC_ROOT,'C:/Users/user/Django-Delivery/mysite/images/'))
    
  #  image = open(path + filename, "wb")

   # image.write(base64.b64decode(face))
   # image.close()
    
    return render(request,'delivery/DeliveryInformation.html', {'information' : data})

class Information():
    #현재 시간 불러옴
    now = datetime.datetime.now()
    
    #현재 년-월-일만 추출
    nowDate = now.strftime('%Y-%m-%d')
    data = Nowcapture.objects.filter(todaydate = nowDate).only('nowpeople')
    
    def get_context_data(seldt, **kwargs):
        context = super().get_context_data(**kwargs)
        context['employee_number'] = Employee.objects.filter(employee_number = data)
    
        return context