from datetime import datetime
from rest_framework.test import APITestCase
from django.test import TestCase, SimpleTestCase
from core.cdr import Transaction, ChargeDetailRecord
from django.shortcuts import reverse


class TestCDR(SimpleTestCase):
    """
        Test cdr class data for calculating total energy and time.
    """
    def setUp(self):
        self.cdr = ChargeDetailRecord(
            start_transaction=Transaction(1204307, datetime.strptime('2021-04-05T10:04:00Z', "%Y-%m-%dT%H:%M:%SZ")),
            stop_transaction=Transaction(1215230, datetime.strptime('2021-04-05T11:27:00Z', "%Y-%m-%dT%H:%M:%SZ")),
        )

    def test_calculate_total_energy(self):
        self.assertEqual(self.cdr.total_energy, 10923)

    def test_calculate_charging_time(self):
        self.assertEqual(self.cdr.charging_time_in_minute, 83)


class TestChargingProcessRating(APITestCase):
    """
        Test charging process rating API for calculating total price.
    """
    def test_charging_process(self):
        data = {
            "rate": {"energy": 0.3, "time": 2, "transaction": 1},
            "cdr": {"meterStart": 1204307, "timestampStart": "2021-04-05T10:04:00Z",
                    "meterStop": 1215230, "timestampStop": "2021-04-05T11:27:00Z"}
        }
        response = self.client.post(reverse('core:rate'), data, format="json")
        self.assertEqual(response.status_code, 200)
