import unittest
from datetime import date, datetime
from bcbapi.services.ptax import PTAX, PTAXService

class TestPtaxApi(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.ptax_service = PTAXService()


    def test_get_ptax_rate_should_return_none(self):
        ptax = self.ptax_service.get_ptax_rate(date(2024, 1, 1))
        self.assertIsNone(ptax)


    def test_get_ptax_rate_should_return_ptax(self):
        ptax = self.ptax_service.get_ptax_rate(date(2024, 1, 2))
        self.assertEqual(ptax, PTAX(
            timestamp=datetime(2024, 1, 2, 13, 5, 50, 319000), 
            buy=4.891, 
            sell=4.8916
        ))

    def test_daily_ptax_rate_by_period_should_return_4(self):
        daily_ptax_rate_by_period = self.ptax_service.get_daily_ptax_rate_by_period(date(2024, 1, 2), date(2024, 1, 5))
        self.assertEqual(len(daily_ptax_rate_by_period), 4)


if __name__ == '__main__':
    unittest.main(verbosity=2)
