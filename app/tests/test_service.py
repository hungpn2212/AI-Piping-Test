from unittest import TestCase
from unittest.mock import patch

from app.service import generate_recommendations
from app.tests.factories import (DEFAULT_RECOMMENDATIONS,
                                 create_fake_openai_response)


class TestService(TestCase):
    @patch('app.service.client.chat.completions.create', return_value=create_fake_openai_response())
    def test_generate_recommendations(self, openai_mock):
        season = 'summer'
        country = 'US'
        recommendations = generate_recommendations(season, country)
        self.assertEqual(recommendations, DEFAULT_RECOMMENDATIONS)
