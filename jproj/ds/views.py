from django.shortcuts import render
from .models import *
from scipy import stats
from django_pandas.io import read_frame
from django.http import HttpResponse  # returns blank web page
import json
from django.core.context_processors import csrf
from sklearn import tree

# Create your views here.
def home(request):
	c = {}
	t = Titanic.objects.all()
	c['data'] = t
	d = read_frame(t)
	children = {}
	c['n_children'] = 'childern ' + str(d[d.age == 'Child']['age'].count())
	c['n_adult'] = 'adult ' + str(d[d.age == 'Adult']['age'].count())
	if request.method == 'POST':

		Y = d[['survived']]
		X = d[["group","sex","age"]]

		X["group"].replace(["1st","2nd","3rd","Crew"],[3,2,1,0],inplace=True)
		X["sex"].replace(["Male","Female"],[1,0],inplace=True)
		X["age"].replace(["Adult", "Child"],[1,0],inplace=True)
		Y["survived"].replace([True,False],[1,0],inplace=True)

		clf = tree.DecisionTreeClassifier()
		clf = clf.fit(X, Y)

		def choices(group,sex,age):
			g = {
				'1st': 3,
				'2nd': 2,
				'3rd': 1,
				'Crew': 0,
			}
			s= {
				'Male': 1,
				'Female': 0,
				
			}
			a = {
				'Adult': 1,
				'Child': 0,
				
			}
			return clf.predict([g[group],s[sex],a[age]])


		group = request.POST['group']
		sex = request.POST['sex']
		age = request.POST['age']
		s = choices(group, sex, age)
		if s:
			c['survived'] = 'will survive'
		else:
			c['survived'] = 'will die'
	return render(request, 'home.html', c)

def gen_o(total, died, title):
	j = {
		'title': title,
		'subtitle': 'died',
		'ranges': [total, total, total],
		'measures': [died,],
		'markers': [died]
	}
	return j

def gen_json(request):
	c = {}
	t = Titanic.objects.all()
	c['data'] = t
	d = read_frame(t)
	n_ch = d[d.age == 'Child']['age'].count()
	n_ch_d = d[(d.age == 'Child') & d.survived]['age'].count()
	children = gen_o(n_ch, n_ch-n_ch_d, 'children')
	
	j = [children]
	#c['n_children'] = 'childern ' + str()
	c['n_adult'] = 'adult ' + str(d[d.age == 'Adult']['age'].count())
	return HttpResponse(json.dumps(j), content_type="application/json") # instead of blank web page it will return json