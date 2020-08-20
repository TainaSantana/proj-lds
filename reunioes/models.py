from django.db import models


class Reuniao(models.Model):

    titulo = models.CharField(max_length=255)
    data_inicio = models.DateTimeField(blank=False, null=False)
    hora_inicio = models.DateTimeField(blank=True, null=True)
    data_fim = models.DateTimeField(blank=False, null=False)
    descricao = models.TextField()
    pauta = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    email = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.titulo


    

