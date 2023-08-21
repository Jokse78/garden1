from django.db import models


class Veisle(models.Model):
    pavadinimas = models.CharField(max_length=100)
    aprasymas = models.TextField()
    #vietove = models.CharField(max_length=100)
    #zeme = models.CharField(max_length=100)
    #iranga = models.CharField(max_length=100)
    Siltnamis = "siltnamis"
    Laukas = "laukas"
    LAUKO_CHOICES = [
        (Siltnamis, 'siltnamis'),
        (Laukas, 'laukas'),
        ]
    siltnamis_ar_laukas = models.CharField(
        max_length=10,
        choices=LAUKO_CHOICES,
        default=Siltnamis,)




class Darzo_darbai(models.Model):
    vartotojas = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    veisle = models.ForeignKey(Veisle, on_delete=models.CASCADE)
    pasodinimo_data = models.DateField()
    sodinimas_is_seklu = models.BooleanField(default=False)
    sodinuku_pikiavimas = models.DateField()
    sodinuku_perkelimas_i_lysvas = models.DateTimeField()
    tresimas = models.DateTimeField()
    laistymas = models.DateTimeField()
    purskimas = models.DateTimeField()
    derliaus_nuemimas = models.DateTimeField()
    pastabos = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Daržo_darbas'
        verbose_name_plural = 'Daržo_darbai'
    class Meta:
        verbose_name = 'Veislė'
        verbose_name_plural = 'Veislės'