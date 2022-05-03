from datetime import datetime
from rest_framework.test import APITestCase
from utils.cdr_method import CDR
from utils.rate_method import Rate


class TestCDRComponent(APITestCase):
    """
        Test data for calculating CDR component.
    """
    def setUp(self):
        self.cdr = CDR().cdr(meter_start=1204307,
                             timestamp_start=datetime.strptime('2021-04-05T10:04:00Z', "%Y-%m-%dT%H:%M:%SZ"),
                             meter_stop=1215230,
                             timestamp_stop=datetime.strptime('2021-04-05T11:27:00Z', "%Y-%m-%dT%H:%M:%SZ"))

    def test_cdr_component(self):
        self.assertEqual(self.cdr, {'consumed_kwh': 10.923, 'consumed_second': 4980})


class TestRateComponent(APITestCase):
    """
        Test data for calculating Rate component.
    """
    def setUp(self):
        self.rate = Rate().rate(energy=0.3, time=2.0, transaction=1.0,
                                cdr_component={'consumed_kwh': 10.923, 'consumed_second': 4980})

    def test_rate_component(self):
        self.assertEqual(self.rate, {"overall": "7.04",
                                     "components": {
                                         "energy": "3.277",
                                         "time": "2.767",
                                         "transaction": 1
                                     }
                                     }
                         )
