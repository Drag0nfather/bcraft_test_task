from djmoney.contrib.django_rest_framework import MoneyField
from rest_framework import serializers

from api.models import Statistic


class StatisticInputSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('date', 'views', 'clicks', 'cost')
        model = Statistic


class StatisticByDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistic
        fields = ('date', 'statistic',)
    statistic = serializers.SerializerMethodField('get_statistic')

    def get_statistic(self, obj):
        statistics = Statistic.objects.filter(date=obj['date'])
        statistic_serializer = StatisticOutputSerializer(statistics, many=True)
        return statistic_serializer.data


class StatisticOutputSerializer(serializers.Serializer):
    date = serializers.DateField()
    views = serializers.IntegerField()
    clicks = serializers.IntegerField()
    cost = MoneyField(
        max_digits=14,
        decimal_places=2,
        default_currency='RUB'
    )
    cpc = MoneyField(
        max_digits=14,
        decimal_places=2,
        default_currency='RUB'
    )
    cpm = MoneyField(
        max_digits=14,
        decimal_places=2,
        default_currency='RUB'
    )
