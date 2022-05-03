from dataclasses import dataclass
from datetime import datetime


@dataclass
class Transaction:
    """
        Data class for a transaction parameters
           "During transaction event a meter value retrieved from the electricity meter along with a timestamp are sent
            by the charging station to the CSMS
                1. meter_value constitutes meter_start and meter_stop
                2. timestamp constitutes timestamp_start and timestamp_stop"
    """
    meter_value: int
    timestamp: datetime


@dataclass
class ChargeDetailRecord:
    """
        Data class for Charging Process parameters
            "During a charging process two important events are sent by the charging station to the CSMS:
                1. start_transaction : constitutes the begin of a charging process
                2. stop_transaction : instructs the CSMS that the charging process has ended "
    """
    start_transaction: Transaction
    stop_transaction: Transaction

    @property
    def total_energy(self):
        """
            Function for calculating the overall consumed energy(in Wh)
        """
        return self.stop_transaction.meter_value - self.start_transaction.meter_value

    @property
    def charging_time_in_minute(self):
        """
            Function for calculating the overall time of the car consumed energy
        """
        return (self.stop_transaction.timestamp - self.start_transaction.timestamp).seconds / 60


