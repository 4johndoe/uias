from django.db import models

class License(models.Model):
    number = models.IntegerField(max_length=6)
    firm = models.CharField(max_length=20)
    kod = models.IntegerField(max_length=10)

    def __unicode__(self):
        # return self.number.__str__() + ' ' + self.firm
        return self.number.__str__()


class Carriage(models.Model):
    lic = models.ForeignKey(License)
    departure_date = models.DateField()
    arrival_date = models.DateField()
    loading_point = models.CharField(max_length=20)
    unloading_point = models.CharField(max_length=20)
    loading_country = models.CharField(max_length=2)
    unloading_country = models.CharField(max_length=2)
    truck_nom = models.CharField(max_length=8)
    trailer_nom = models.CharField(max_length=8)
    country_of_reg = models.CharField(max_length=2)
    weight = models.IntegerField(default=0)
    speedometr_before = models.IntegerField()
    speedometr_after = models.IntegerField()
    etc = models.IntegerField()

    def __unicode__(self):
        pass