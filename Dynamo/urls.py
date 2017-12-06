from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import url
from .import views


app_name = 'Dynamo'

urlpatterns = [
    #Dynamo-add
    url(r'item/add/$',views.ItemCreate.as_view(),name='Dynamo-add'),

]
