from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_http_methods
from django.views.generic import TemplateView

from .models import newItem

#@require_http_methods("POST")
def index(request):
	#return HttpResponse("shop works")
	return render(request, 'mycode/index-enter-to-shop.html')

#@require_http_methods("POST")
class ShopView(TemplateView):
	template_name = 'mycode/shop-offer.html'

	def POST(self, request):
		table_list = newItem.objects.all()
		context={'table_list': table_list}
		return render(request, self.template_name, context)
		 