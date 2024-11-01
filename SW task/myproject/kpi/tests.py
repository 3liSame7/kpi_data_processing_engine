from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
# from .models import KPI

class KPIAPITests(APITestCase):
    def test_create_kpi(self):
        url = reverse('kpi-list')
        data = {"name": "Sample KPI", "expression": "ATTR+50"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_kpis(self):
        url = reverse('kpi-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
