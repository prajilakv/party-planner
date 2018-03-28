from .models import Finance, Guests
from rest_framework import serializers


class GuestsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Guests
        fields = ('invited_family', 'adults', 'children', 'status')


class FinanceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Finance
        fields = ('item', 'price')
