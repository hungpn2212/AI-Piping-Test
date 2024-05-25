from unittest import TestCase
from unittest.mock import patch

from fastapi import status
from fastapi.testclient import TestClient

from app.constants import COUNTRY_MAPPINGS
from app.main import app
from app.tests.factories import create_fake_openai_response


class TestApp(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.client = TestClient(app)

    def test_recommendation__invalid_country(self):
        response = self.client.get(
            '/recommendations?season=summer&country=invalid_country')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json(), {'message': 'Invalid country'})

    def test_recommendation__invalid_season(self):
        response = self.client.get(
            '/recommendations?season=invalid_season&country=US')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json(), {'message': 'Invalid season'})

    @patch('app.service.client.chat.completions.create', return_value=create_fake_openai_response())
    def test_recommendation__success(self, openapi_mock):
        season = 'summer'
        country_code = 'US'
        response = self.client.get(
            f'/recommendations?season={season}&country={country_code}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            {
                'country': COUNTRY_MAPPINGS[country_code.upper()],
                'season': season,
                'recommendations': ['Visit the beach', 'Visit the mountains', 'Visit the forest'],
            }
        )

    @patch('app.service.client.chat.completions.create', return_value=create_fake_openai_response())
    def test_recommendation__case_sensitive_country_code(self, openapi_mock):
        response = self.client.get('/recommendations?season=summer&country=uS')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
