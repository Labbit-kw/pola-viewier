# form django.contrib import admin
from django.urls import path
from . import views
# from django.conf.urls import url
# from.views import DbFilter_list

urlpatterns = [

    path('',views.home,name='home'),
    path('dbcall/', views.list_db_func, name='dbcall'),
]
