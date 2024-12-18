from rest_framework import serializers
from versatileimagefield.serializers import VersatileImageFieldSerializer
from .models import ImageModel, Horoscope

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

class HoroscopeSerializer(serializers.ModelSerializer):
    zodiac_id = serializers.SerializerMethodField()
    zodiac_name = serializers.SerializerMethodField()
    
    class Meta:
        model = Horoscope
        fields = ['date', 'zodiac_id','zodiac_name','description']

    def get_zodiac_id(self, ins):
        return f'{ins.zodiac.id}'

    def get_zodiac_name(self, ins):
        return f'{ins.zodiac.name}'