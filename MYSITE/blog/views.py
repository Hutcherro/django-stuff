from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	#return render(request, 'blog/simple.html')
	return render(request, 'blog/index.html')
	#return HttpResponse('dziala')

def detail(request):
	return render(request, 'blog/name.html')

def get_name(request):
	if request.method == 'POST':
		form = NameForm(request.POST)
		if form.is_valid():
			return HttpResponseRedirect('/thanks/')
	else:
		form = NameForm()
	return render(request, 'blog/name.html', {'form': form})