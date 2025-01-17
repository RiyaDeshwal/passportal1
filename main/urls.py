from django.urls import path
from . import views

urlpatterns = [
  path('',views.home, name="home"),
  path('api/data/', views.get_data, name='get_data'),
  path('otp/', views.otp , name="otp"),
  path('verify/', views.sendOtp, name='send_otp'),
  path('submit/', views.verify_otp, name='verify_otp'),
  path('register/', views.savedata, name='register'),
  path('Order_Summary/', views.Order_Summary, name='Order_Summary'),
  path('api/',views.user_data,name='api'),
]
