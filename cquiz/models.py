from django.db import models

# Create your models here.
class python(models.Model):
	ques= models.CharField(max_length=100)
	img= models.ImageField(upload_to='pics')
	opt1= models.CharField(max_length=20)
	opt2= models.CharField(max_length=20)
	opt3= models.CharField(max_length=20)
	opt4= models.CharField(max_length=20)
	corr= models.CharField(max_length=20)
