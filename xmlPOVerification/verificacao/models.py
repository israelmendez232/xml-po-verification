from django.db import models

# Create your models here.
class Verificação():
    xml = models.FileField('Insira aqui o XML:', upload_to='XMLs', blank=True)    
    po = models.FileField('Insira aqui a Ordem de COmpra:', upload_to='POs', blank=True)    
    def __str__(self):        
        return self.titulo
        