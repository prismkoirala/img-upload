# authentication.py
from rest_framework import authentication
from rest_framework import exceptions
from django.conf import settings
from urllib.parse import urlparse
from .models import Client

class ClientAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        origin = request.META.get('HTTP_ORIGIN')
        print('origin: ', origin)
        if not origin:
            raise exceptions.AuthenticationFailed('No Origin header provided.')

        parsed_origin = urlparse(origin)
        domain = parsed_origin.netloc
        print(domain)
        
        if not domain:
            raise exceptions.AuthenticationFailed('Invalid Origin header.')

        try:
            client = Client.objects.get(domain=domain)
        except Client.DoesNotExist:
            raise exceptions.AuthenticationFailed('Domain not authorized.')

        secret_key = request.META.get('HTTP_X_SECRET_KEY')
        if not secret_key:
            raise exceptions.AuthenticationFailed('No secret key provided.')

        if secret_key != client.secret_key:
            raise exceptions.AuthenticationFailed('Invalid secret key.')

        return (client, None)

    def has_permission(self, request, view):
        # Here, you might want to reuse the logic from authenticate for simplicity
        try:
            self.authenticate(request)
            return True
        except exceptions.AuthenticationFailed:
            return False