from django.http import JsonResponse
from .models import Drink
from .serializers import Drinkserializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def Drink_list(request):
    if request.method == 'GET':
        drinks = Drink.objects.all()
        serializer = Drinkserializer(drinks, many = True)
        return JsonResponse({'drinks':serializer.data}, safe = False)
    if request.method == 'POST':
        serializer=Drinkserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])
def Drink_details(request,id):
    try:
        drink_using_id = Drink.objects.get(pk=id)
    except Drink.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = Drinkserializer(drink_using_id)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = Drinkserializer(drink_using_id, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        Drink.delete(drink_using_id)
        return Response(status=status.HTTP_202_ACCEPTED)