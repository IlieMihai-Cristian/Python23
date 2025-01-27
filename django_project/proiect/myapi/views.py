from django.shortcuts import render
from rest_framework import viewsets

from aplicatie1.models import Location
from myapi.serializers import LocationSerializer


class LocationViewSet(viewsets.ModelViewSet):
    print('intra')
    # list
    # create
    # retrive (pk)
    # update (pk)
    # destroy (pk)
    queryset = Location.objects.all()
    serializer_class = LocationSerializer