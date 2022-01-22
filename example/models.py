from django.db import models

# Create your models here.
class Simple(models.Model):
    # um atributo é uma coluna da tabela. todos os objetos/linhas teem uma pk
    text = models.CharField(max_length=20)
    number = models.IntegerField(null=True)
    url = models.URLField(default='www.example.com')
