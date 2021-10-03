from django.conf.urls import url

from api.views import StatisticViewSet

urlpatterns = [
    url('statistic/', StatisticViewSet.as_view(
        {
            'post': 'add_statistic',
            'get': 'get_statistic',
            'delete': 'delete_statistic'
        }))
]
