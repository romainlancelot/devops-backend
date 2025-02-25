from django.test import TestCase
from rest_framework.response import Response


class HealthCheckTestCase(TestCase):
    def test_healthcheck_view(self) -> None:
        response: Response = self.client.get("/healthcheck")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), dict(status="ok"))
