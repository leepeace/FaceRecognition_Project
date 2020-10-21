from django.shortcuts import render
from django.http import JsonResponse
from .models import Capture,Employee
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import os
import base64
from django.conf import settings

# Create your views here.

def CapturePage(request):
    return render(request, 'face/CapturePage.html')


@csrf_exempt
def storeBinary(request):
    # POST 요청인 경우
    if request.method == "POST":
        face = request.POST.get('face')
        face = face[22:]#'data:image/png;base64'부분을 제거

        #데이터 db에 저장
        data = Capture(face,request.POST.get('employee_number'))
        data.save()

        #캡쳐사진 경로에 저장
        path = str(os.path.join(settings.STATIC_ROOT,'C:/Users/user/Django-Delivery/mysite/images/'))
        filename = 'test.png'

        image = open(path+filename,"wb")

        image.write(base64.b64decode(face))
        image.close()

        answer = {'filename' : filename}
        return JsonResponse(answer)
        