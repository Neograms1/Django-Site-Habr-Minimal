from django.shortcuts import render,HttpResponse
from .models import TipaChat
from django.views.generic import DetailView



# Create your views here.
def index(request):
	data = TipaChat.objects.all()
	return render(request,'main/index.html',{'data':data})


class NewsDetaiView(DetailView):
	model = TipaChat
	template_name = 'main/news.html'
	context_object_name = 'tipa'

def create(request):
	return render('main/create.html')

def about(request):
	return HttpResponse('<h3>Hello</h3>')
