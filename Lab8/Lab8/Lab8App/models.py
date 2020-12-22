from django.db import models

class Browser(models.Model):
	id=models.AutoField(primary_key=True)
	name=models.CharField(max_length=100)
	country=models.CharField(max_length=50)
	site_url=models.CharField(max_length=100)
	img=models.CharField(max_length=100)

# Create your models here.
