from django.db import models

class Equipamentos(models.Model):
    notebook = models.IntegerField()
    projetor = models.IntegerField()
    camera_fotorgrafica = models.IntegerField()
    tripe_camera = models.IntegerField()
    font_caix_som = models.IntegerField()
    microfone = models.IntegerField()
    caneta_lousa_interativa = models.IntegerField()
    controle_tv = models.IntegerField()
    controle_projetor = models.IntegerField()

class Agendamento(models.Model):
    equipamentos = models.OneToOneField(Equipamentos, related_name="equipamentos", on_delete=models.CASCADE, primary_key=True)
    prof_instrutor = models.CharField(max_length=40)
    sala = models.CharField(max_length=20)
    turno = models.CharField(max_length=5)
    data = models.DateField()