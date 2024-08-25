from django.db import models

# Create your models here.

class UPSC_Books(models.Model):
    subject=models.CharField(max_length=50)
    bookname=models.CharField(max_length=100)
    authorname=models.CharField(max_length=100)
    price=models.IntegerField()
    
    