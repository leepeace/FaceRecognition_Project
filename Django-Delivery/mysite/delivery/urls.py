from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'delivery'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='delivery/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('DeliveryInformation/', views.DeliveryInformation, name='DeliveryInformation'),
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
