from django.db import models


class Veisle(models.Model):
    pavadinimas = models.CharField(max_length=100)
    aprasymas = models.TextField()
    #vietove = models.CharField(max_length=100)
    #zeme = models.CharField(max_length=100)
    #iranga = models.CharField(max_length=100)
    siltnamis_ar_laukas = models.CharField(max_length=100)


class Darzas(models.Model):
    vartotojas = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    veisle = models.ForeignKey(Veisle, on_delete=models.CASCADE)
    plotas = models.DecimalField(max_digits=5, decimal_places=2)
    pasodinimo_data = models.DateField()
    sodinimas_is_seklu = models.BooleanField(default=False)
    sodinuku_pikiavimas = models.DateField()
    sodinuku_perkelimas_i_lysvas = models.DateTimeField()
    tresimas = models.DateTimeField()
    laistymas = models.DateTimeField()
    purkimas = models.DateTimeField()
    derliaus_nuemimas = models.DateTimeField()
    pastabos = models.TextField()

