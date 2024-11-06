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