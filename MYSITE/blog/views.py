from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	#return render(request, 'blog/simple.html')
	return render(request, 'blog/index.html')
	#return HttpResponse('dziala')

def detail(request):
	return HttpResponse("nastepna sciezka")