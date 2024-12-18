from django.db import models
from versatileimagefield.fields import VersatileImageField

def upload_to_folder(instance, filename):
    return f'/{instance.img_id}/images/{filename}'

class ImageModel(models.Model):

    img_id = models.CharField(max_length=20, unique=True)    
    form_task = models.CharField(max_length=100)    
    # encrypt = models.IntegerField(default=1, primary_key=True) 
    image = VersatileImageField(upload_to=upload_to_folder)

    def __str__(self):
        return f'{self.id}'
    
class Client(models.Model):
    name = models.CharField(max_length=100)
    secret_key = models.CharField(max_length=255, unique=True)
    domain = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Zodiac(models.Model):
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=100)


    def __str__(self):
        return self.name

class Horoscope(models.Model):

    zodiac = models.ForeignKey(
        Zodiac,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
    )
    date = models.DateField(auto_now=False, blank=False, null=False)
    description = models.TextField(blank=False, null=False)

    def __str__(self):
        return self.zodiac.name
    