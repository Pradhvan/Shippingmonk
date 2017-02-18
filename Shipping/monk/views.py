from django.shortcuts import render,redirect
from .forms import orderDetailForm,shopForm


# Create your views here.

def hubform(request):
	# if request.method == 'POST':
	# 	form = shopForm(request.POST)
	# 	if form.is_valid():
	# 		post = form.save(commit = False)
	# 		post.save()
	# 		return redirect('/')
	# else:
	renderform = shopForm()
	return render(request,'userinput.html',{'renderform':renderform})


def search(request):
	if request.method == 'POST':
		query = request.POST.get('query')
