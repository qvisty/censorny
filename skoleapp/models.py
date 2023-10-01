from django.db import models

class Skole(models.Model):
    navn = models.CharField(max_length=255)

class Fag(models.Model):
    navn = models.CharField(max_length=255)

class Skoleklasse(models.Model):
    navn = models.CharField(max_length=255)
    skole = models.ForeignKey(Skole, on_delete=models.CASCADE)

class Eksamen(models.Model):
    fag = models.ForeignKey(Fag, on_delete=models.CASCADE)
    skoleklasse = models.ForeignKey(Skoleklasse, on_delete=models.CASCADE)
    dato = models.DateField(null=True, blank=True)

class Personale(models.Model):
    navn = models.CharField(max_length=255)
    skole = models.ForeignKey(Skole, on_delete=models.CASCADE)

class WishDates(models.Model):
    date = models.DateField()
    exam = models.ForeignKey(Eksamen, null=True, blank=True, on_delete=models.CASCADE)
    censor = models.ForeignKey(Personale, null=True, blank=True, on_delete=models.CASCADE)
