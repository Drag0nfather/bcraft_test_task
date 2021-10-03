from rest_framework import status
from rest_framework.test import APITestCase
from datetime import date
from random import randint
from .models import Statistic

TODAY = date.today()

BODY = {
    'date': str(TODAY),
    'views': randint(1, 9999),
    'clicks': randint(1, 9999),
    'cost': randint(1, 9999)
}


class StatisticTestCase(APITestCase):
    def test_post(self):
        """
        Тест Post-запроса
        """
        first_len = Statistic.objects.count()
        # Post-запрос с полными данными
        post = self.client.post('/statistic/', data=BODY)
        self.assertEqual(post.status_code, status.HTTP_201_CREATED)
        second_len = Statistic.objects.count()
        # Post-запрос только с датой
        post = self.client.post('/statistic/', {'date': str(TODAY)})
        self.assertEqual(post.status_code, status.HTTP_201_CREATED)
        third_len = Statistic.objects.count()
        # Проверка, что создалось 2 объекта в БД
        self.assertNotEqual(first_len, second_len, third_len)

    def test_get(self):
        """
        Тест Get-запроса
        """
        # 2 Post-запроса с разными датами: сегодня и год назад
        post = self.client.post('/statistic/', data=BODY)
        post_2 = self.client.post('/statistic/', {'date': '2020-10-01'})
        # Проверка, что посты выдаются
        get = self.client.get('/statistic/')
        self.assertEqual(get.status_code, status.HTTP_200_OK)
        self.assertEqual(len(get.data), 2)
        # Проверка, что работают Query from и to
        get = self.client.get(f'/statistic/?from={TODAY}&to={TODAY}')
        self.assertEqual(get.status_code, status.HTTP_200_OK)
        self.assertEqual(len(get.data), 1)

    def test_delete(self):
        """
        Тест Delete-запроса
        """
        post = self.client.post('/statistic/', data=BODY)
        len = Statistic.objects.count()
        delete = self.client.delete('/statistic/')
        len2 = Statistic.objects.count()
        self.assertEqual(delete.status_code, status.HTTP_410_GONE)
        self.assertNotEqual(len, len2)
