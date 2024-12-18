from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.models import ImageModel, Horoscope
from core.serializers import ImageModelSerializer, HoroscopeSerializer
from core.authentication import ClientAuthentication

class HomeView(APIView):
    def get(self, request):
        return Response({"message": "Came to api!"}, status=status.HTTP_200_OK)

class HoroscopeView(APIView):
    permission_classes = [ClientAuthentication]

    def get(self, request):
        date = request.query_params.get('date')  
        zodiac_id = request.query_params.get('zodiac_id') 

        horoscopes = Horoscope.objects.all()

        if date:
            horoscopes = horoscopes.filter(date=date)

        if zodiac_id:
            horoscopes = horoscopes.filter(zodiac_id=zodiac_id)
            
        serializer = HoroscopeSerializer(horoscopes, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)


class ImageModelView(APIView):
    local_encrypt_value = "f6ac81e38ef4aa5ddea04866bfe096c9" 

    def validate_encrypt(self, request):
        encrypt_value = request.query_params.get('encrypt') if request.method == 'GET' else request.data.get('encrypt')

        if encrypt_value != self.local_encrypt_value:
            return Response({"error": "Forbidden: invalid encrypt value."}, status=status.HTTP_403_FORBIDDEN)
        return None

    def get(self, request, *args, **kwargs):
        validation_response = self.validate_encrypt(request)
        if validation_response:
            return validation_response
    
        queryset = ImageModel.objects.all()
        serializer = ImageModelSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        validation_response = self.validate_encrypt(request)
        if validation_response:
            return validation_response
    
        serializer = ImageModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        validation_response = self.validate_encrypt(request)
        if validation_response:
            return validation_response
    
        instance_id = request.data.get('id')
        try:
            instance = ImageModel.objects.get(id=instance_id)
        except ImageModel.DoesNotExist:
            return Response({"error": "Instance not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ImageModelSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):

        instance_img_id = request.data.get('img_id')
        try:
            instance = ImageModel.objects.get(img_id=instance_img_id)
        except ImageModel.DoesNotExist:
            return Response({"error": "Instance not found"}, status=status.HTTP_404_NOT_FOUND)
        
        instance.delete()
        return Response({"message": "Instance deleted successfully"}, status=status.HTTP_204_NO_CONTENT)