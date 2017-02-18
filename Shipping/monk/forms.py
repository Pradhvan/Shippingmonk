from django import forms as forms
from django.forms import ModelForm
from .models import orderDetail,shop

class orderDetailForm(forms.Form):
	class Meta:
		model = orderDetail
		fields = ('name','Address','orderId')


class shopForm(forms.Form):
	class Meta:
		model = shop
		fields = ('hname','hubid','address','Auth_to','email','phone_number')