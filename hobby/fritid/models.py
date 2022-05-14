from django.db import models
from django.utils import timezone

# Create your models here.
class Hobby(models.Model):
    titel = models.CharField(max_length=50)
    beskrivelse = models.TextField()
    kategori = models.ManyToManyField('Kategori', related_name='item')
    img = models.ImageField(upload_to='menu_images/')
    tilbehør = models.TextField(max_length=100)
    link1 = models.URLField(blank=True, null=True)
    link2 = models.URLField(blank=True, null=True)
    pris = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.titel

class Kategori(models.Model):
    titel = models.CharField(max_length=50)

    def __str__(self):
        return self.titel

class SlagsModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    pris = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    items = models.ManyToManyField(
        'Hobby', related_name='slags', blank=True)
    navn = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=50, blank=True)
    by = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f'Slags: {self.created_on.strftime("%b %d %I: %M %p")}'

class Kommentar(models.Model):
    kommentar = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)


