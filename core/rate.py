from dataclasses import dataclass
from decimal import Decimal

@dataclass
class Rate:
    """
        Data class for a charging process rating parameters
           "Rating is the process of applying a rate to a CDR.
            A rate can have the following components
                1. energy: rate the charging process based on the energy consumed
                2. time: rate the charging process based on its duration
                3. transaction: fees per charging process "
    """
    energy: float
    time: float
    transaction: float

