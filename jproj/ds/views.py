from django.shortcuts import render
from .models import *
from scipy import stats
from django_pandas.io import read_frame

# Create your views here.
def home(request):
	context = {}
	t = Titanic.objects.all()
	context['data'] = t
	df = read_frame(t)
	return render(request, 'home.html', context)

#df = DataFrame('data', index=index)