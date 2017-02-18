from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.hubform, name='User_input_form'),
]