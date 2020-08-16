from django.db import models

# Create your models here.
class accpython(models.Model):
	ques= models.CharField(max_length=100)
	img= models.ImageField(upload_to='pics',blank=True,default="")
	opt1= models.CharField(max_length=100)
	opt2= models.CharField(max_length=100)
	opt3= models.CharField(max_length=100)
	opt4= models.CharField(max_length=100)
	corr= models.CharField(max_length=100)

class record(models.Model):
	user=models.CharField(max_length=100)
	marks=models.CharField(max_length=100)
	date=models.DateTimeField()
