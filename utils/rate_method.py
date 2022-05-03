
class Rate:
    """
        Class for calculate rate component values and total price for the car consumed energy
    """
    def rate(self, energy: float, time: float, transaction: float, cdr_component: dict) -> dict:
        """
            Inputs:
                energy: float,              sample: 0.3
                time: float,                sample: 2.0
                transaction: float,         sample: 1.0
                cdr_component: dict,        sample: {'consumed_kwh': 11, 'consumed_second': 4980}

            Output:
                {
                "overall": "7.04",
                "components": {
                    "energy": "3.277",
                    "time": "2.767",
                    "transaction": 1
                }
        """
        energy_price = energy * cdr_component['consumed_kwh']
        energy_price_rounded = "{:.3f}".format(energy_price)

        time_price = cdr_component['consumed_second'] / 3600 * time
        time_price_rounded = "{:.3f}".format(time_price)
        total_price = "{:.2f}".format(energy_price + time_price + transaction)

        rate_component = {
            'overall': total_price,
            'components': {
                "energy": energy_price_rounded,
                "time": time_price_rounded,
                "transaction": transaction
            }
        }
        return rate_component
