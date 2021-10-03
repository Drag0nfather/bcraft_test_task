from typing import Optional

from django.db import models
from djmoney.models.fields import MoneyField


class Statistic(models.Model):

    def __str__(self):
        return f'Статистика № {self.id} за дату {self.date}'

    date = models.DateField()
    views = models.IntegerField(
        blank=True,
        null=True
    )
    clicks = models.IntegerField(
        blank=True,
        null=True
    )
    cost = MoneyField(
        max_digits=14,
        decimal_places=2,
        default_currency='RUB',
        blank=True,
        null=True
    )

    @property
    def cpc(self) -> Optional[float]:
        cost = self.cost
        clicks = self.clicks
        return cost / clicks if cost and clicks else None

    @property
    def cpm(self) -> Optional[float]:
        cost = self.cost
        views = self.views
        return cost / views * 1000 if cost and views else None
