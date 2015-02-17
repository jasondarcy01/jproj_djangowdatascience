import urllib2
import csv 
from ds.models import Titanic

#in future, create script that will call python manage.py import.csv to run at midnight everynight

def import_csv():
	url = 'http://vincentarelbundock.github.io/Rdatasets/csv/datasets/Titanic.csv'
	
	try:
		connect = urllib2.urlopen(url)

		# csv module did not parse data received with connect.read() correctly. Changing to connect.readlines() solved the promblem
		data = connect.readlines()

		connect.close()

		# csv.reader(data) just parses the data (and the first line is considered as just data)
		# while csv.DictReader(data) considers the first line as a header and excludes it and also allows to store key-value pairs
		csv_data = csv.DictReader(data)

		# removes previous records
		Titanic.objects.all().delete()

		for row in csv_data:
			new_obj = {
				'group': row['Class'],
				'sex': row['Sex'],
				'age': row['Age'],
				'freq': row['Freq']
			}
			if row['Survived'] == 'Yes':
				new_obj['survived'] = True
			else:
				new_obj['survived'] = False
			Titanic.objects.create(**new_obj)	#Titanic.objects.create(group=row['Class'], sex=row['Sex'] ..., ..)
	
	except urllib2.HTTPError, e:
		pass


# def sdfsf():
# 	a = Titanic.objects.all()
# 	df = pd.DataFrame(a)
# 	var1 = df[group]
# 	var2 = df[group].mean()
# 	var3 = df[group].hist()
# 	var4 = sklearn decision tree 'who more likely to survive'
# 	finally display on browser templates and views hold var1, var2, etc..

# Anaconda pacakeges, i.e. numpy are not recognized with python running seperately from Anaconda
# Therefore I will remove python2.7 from the path -> C:\Python27;C:\Python27\Scripts;