from datetime import datetime


class CDR:
    """
        Class for calculate CDR(charge detail record) component values
    """
    def cdr(self, meter_start: int, timestamp_start: datetime, meter_stop: int, timestamp_stop: datetime) -> dict:
        """
            Inputs:
                meter_start: int,            sample: 1204307
                timestamp_start: datetime,   sample: "2021-04-05T10:04:00Z"
                meter_stop: int,             sample: 1215230
                timestamp_stop: datetime,    sample: "2021-04-05T11:27:00Z"

            Output:
                {
                'consumed_kwh': 10.923,
                'consumed_second': 4980
                 }
        """
        consumed_kwh = (meter_stop - meter_start) / 1000
        consumed_second = (timestamp_stop - timestamp_start).seconds

        cdr_component = {
            'consumed_kwh': consumed_kwh,
            'consumed_second': consumed_second
        }
        return cdr_component



