import unittest
from datetime import date
from bcbapi import ExchangeRateService

class TestExchangeRate(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.service = ExchangeRateService()

    def test_get_ptax_rate_should_return_none(self):
        result = self.service.get_exchange_rate("CAD", date(2024, 1, 1))
        self.assertIsNone(result)

    def test_get_ptax_rate_should_return_5(self):
        result = self.service.get_exchange_rate("CAD", date(2024, 1, 8))
        self.assertEqual(len(result), 5)

    def test_get_daily_exchange_rate_by_period_should_return_10(self):
        result = self.service.get_daily_exchange_rate_by_period(
            "CAD", date(2024, 8, 1), date(2024, 8, 2)
        )
        self.assertEqual(len(result), 10)


if __name__ == '__main__':
    unittest.main(verbosity=2)
