from django.urls import path

from . import views

app_name = 'FaceRecognition'

urlpatterns = [
    path('CapturePage/', views.CapturePage, name='CapturePage'),
    path('storeBinary/', views.storeBinary, name='storeBinary'),
]