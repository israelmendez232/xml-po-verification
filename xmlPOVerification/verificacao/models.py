from django.db import models
from datetime import datetime

# Create your models here.
class Verificação(models.Model):
    datetime =  datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    xml = models.FileField('XML:', upload_to='XMLs', blank=True)    
    po = models.FileField('Ordem de Compra:', upload_to='POs', blank=True)   
    def __str__(self):        
        return self.datetime
