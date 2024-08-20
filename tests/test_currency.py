import unittest
from bcbapi import CurrencyService, Currency

class TestCurrency(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.service = CurrencyService()

    def test_get_currencies_should_return_all(self):
        result = self.service.get_all()
        self.assertEqual(len(result), 10)

    def test_get_currencies_should_contain_cad(self):
        result = self.service.get_all()
        cad_currency = next((currency
                             for currency in result
                             if currency.code == 'CAD'), None)
        self.assertIsInstance(cad_currency, Currency)


if __name__ == '__main__':
    unittest.main(verbosity=2)
