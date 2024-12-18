from django.contrib import admin

from .models import ImageModel, Zodiac, Horoscope, Client

admin.site.register(ImageModel)
admin.site.register(Zodiac)
admin.site.register(Horoscope)
admin.site.register(Client)
