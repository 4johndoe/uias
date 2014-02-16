from django.db import models

class Firm(models.Model):
    name = models.CharField(max_length=100)
    edrpo = models.IntegerField(default=0, max_length=8)
    amount = models.IntegerField(default=0, max_length=3)

    def __unicode__(self):
        return self.name

class LicenseBook(models.Model):
    firm = models.ForeignKey(Firm)
    number = models.IntegerField(default=0)

    def __unicode__(self):
        return self.number

class Carriage(models.Model):
    _license = models.ForeignKey(LicenseBook)
    departure_date = models.DateField('departure_date')
    arrival_date = models.DateField('arrival_date')
    loading_point = models.CharField(max_length=20)
    unloading_point = models.CharField(max_length=20)
    loading_country = models.CharField(max_length=2)
    unloading_country = models.CharField(max_length=2)
    truck_nom = models.CharField(max_length=8)
    trailer_nom = models.CharField(max_length=8)
    country = models.CharField(max_length=2)
    weight = models.IntegerField(default=0)
    speedometr_before = models.IntegerField(default=0)
    speedometr_after = models.IntegerField(default=0)
    etc = models.IntegerField(default=0)
