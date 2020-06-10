from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *

class ClassList(APIView):
    def get(self, request):
        model = ClassLocation.objects.all()
        serializer = ClassLocationSerializer(model, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ClassLocationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ParticularLocation(APIView):
    def get(self, request, class_id):
    #def get(self, request, NameOfClass):
        try:
            model = ClassLocation.objects.get(id=class_id)
        except ClassLocation.DoesNotExist:
            return Response(f'Class_id {class_id} Not Found in database', status=status.HTTP_204_NO_CONTENT)
            #model = ClassLocation.objects.get(id=NameOfClass)
        serializer = LocationSerializer(model)
        return Response(serializer.data) 

    def delete(self, request, class_id):
        try:
            model = ClassLocation.objects.get(id=class_id)
        except ClassLocation.DoesNotExist:
            return Response(f'Class_id {class_id} Not Found in database', status=status.HTTP_204_NO_CONTENT)
        model.delete()
        return Response(status=status.HTTP_200_OK)      