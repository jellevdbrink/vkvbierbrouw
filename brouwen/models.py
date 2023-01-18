from django.db import models

MOUT_TYPES = [
    ('grain', 'Grain'),
    ('sugar', 'Sugar'),
]
GIST_TYPES = [
    ('L', 'L'),
    ('D', 'D'),
]
GIST_MERKEN = [
    ('lallemand', 'Lallemand'),
    ('white_labs', 'White labs'),
    ('siebel', 'Siebel Inst'),
    ('wyeast', 'Wyeast'),
    ('east_coast_yeast', 'East Coast Yeast'),
    ('mangrove_jack', 'Mangrove Jack'),
    ('brewferm', 'Brewferm'),
    ('coopers', 'Coopers'),
    ('real_brewers_yeast', 'Real Brewers Yeast'),
    ('muntons', 'Muntons'),
    ('fermentis', 'Fermentis'),
]
GIST_FLOCS = [
    ('low', 'Low'),
    ('low_medium', 'Low/Medium'),
    ('medium', 'Medium'),
    ('medium_high', 'Medium/High'),
    ('high', 'High'),
]


class Brouwer(models.Model):
    voornaam = models.CharField(max_length=50)
    achternaam = models.CharField(max_length=100)
    gebrouwen = models.IntegerField(verbose_name='Gebrouwen bieren', default=0)

    class Meta:
        verbose_name = 'Brouwer'
        verbose_name_plural = 'Brouwers'

    def get_volledige_naam(self):
        return f'{self.voornaam} {self.achternaam}'

    def __str__(self):
        return self.get_volledige_naam()


class Mout(models.Model):
    naam = models.CharField(max_length=150)
    type = models.CharField(max_length=50, choices=MOUT_TYPES)
    max_sg = models.DecimalField(max_digits=4, decimal_places=3)
    lovibond = models.DecimalField(decimal_places=1, max_digits=5)
    beschrijving = models.TextField()
    voorraad = models.IntegerField()
    prijs = models.DecimalField(decimal_places=2, max_digits=5, help_text='per kg')

    class Meta:
        verbose_name = 'Mout'
        verbose_name_plural = 'Mouten'

    def __str__(self):
        return self.naam


class Hop(models.Model):
    naam = models.CharField(max_length=150)

    class Meta:
        verbose_name = 'Hop'
        verbose_name_plural = 'Hoppen'

    def __str__(self):
        return self.naam


class Gist(models.Model):
    naam = models.CharField(max_length=150)
    type = models.CharField(max_length=1, choices=GIST_TYPES)
    merk = models.CharField(max_length=100, choices=GIST_MERKEN)
    floc = models.CharField(max_length=100, choices=GIST_FLOCS)

    class Meta:
        verbose_name = 'Gist'
        verbose_name_plural = 'Gisten'

    def __str__(self):
        return self.naam
