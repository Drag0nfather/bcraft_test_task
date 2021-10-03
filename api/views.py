from rest_framework import status, viewsets
from rest_framework.response import Response

from api.models import Statistic
from api.serializers import (
    StatisticInputSerializer,
    StatisticByDateSerializer
)


class StatisticViewSet(viewsets.ViewSet):

    def add_statistic(self, request) -> Response:
        """
        Метод добавления статистики. Принимает обязательное
        поле date, и 3 необязательных поля: views, clicks and cost
        """

        data = request.data
        serializer = StatisticInputSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            data=data,
            status=status.HTTP_201_CREATED
        )

    def get_statistic(self, request) -> Response:
        """
        Метод показа всей статистики, группирует статистику по датам.
        Может принимать на вход query параметры from и to, и показывать
        статистку за этот период
        """
        start_date = self.request.query_params.get('from')
        end_date = self.request.query_params.get('to')
        if start_date and end_date:
            queryset = Statistic.objects.filter(
                date__gte=start_date,
                date__lte=end_date
            ).order_by('date').values('date').distinct()
        else:
            queryset = Statistic.objects.order_by(
                'date').values('date').distinct()
        serializer = StatisticByDateSerializer(queryset, many=True)
        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK
        )

    def delete_statistic(self, request) -> Response:
        """
        Метод удаления всей статистики
        """
        deleted_queryset = Statistic.objects.all().delete()
        return Response(
            data={'delete': 'success'},
            status=status.HTTP_410_GONE
        )
