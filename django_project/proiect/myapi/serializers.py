from rest_framework import serializers

from aplicatie1.models import Location


class LocationSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Location
        fields = ['city', 'country']