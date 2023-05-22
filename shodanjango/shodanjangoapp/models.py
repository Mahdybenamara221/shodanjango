from django.db import models

# Create your models here.

class information(models.Model):
    ip=models.CharField(max_length=100,primary_key=True,default='')
    org=models.CharField(max_length=100,default='')
    os=models.CharField(max_length=100,default='')
    country=models.CharField(max_length=100,default='')
    city=models.CharField(max_length=100,default='')
    def __str__(self):
        return "%s"%(self.ip)
    class Meta:
        db_table="Info"


class address(models.Model):
    ip=models.CharField(max_length=100)
    class Meta:
        db_table="Address"