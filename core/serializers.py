from rest_framework import serializers
from versatileimagefield.serializers import VersatileImageFieldSerializer
from .models import ImageModel

class ImageModelSerializer(serializers.ModelSerializer):
    image = VersatileImageFieldSerializer(
        sizes=[
            ('small', 'crop__100x100'),
            ('medium', 'crop__300x300'),
            ('original', 'url'),
        ]
    )
    class Meta:
        model = ImageModel
        fields = ['img_id', 'form_task', 'image']

    # def validate_encrypt(self, value):
    #     # Check if the incoming encrypt value matches the local_encrypt_value
    #     if value != self.local_encrypt_value:
    #         raise serializers.ValidationError("Unauthorized access: encrypt value does not match.")
    #     return value