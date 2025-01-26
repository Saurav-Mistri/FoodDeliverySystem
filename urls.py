from django.urls import path
from  . import views

urlpatterns = [
    path('', views.add_cust_page),
    path('add_cust_page', views.add_cust_page),
    path('add_cust_func', views.add_cust_func),
    path('dashboard',views.dashboard)

]