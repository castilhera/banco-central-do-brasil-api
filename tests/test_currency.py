import unittest
from bcbapi.services.currency import CurrencyService, Currency

class TestCurrencyApi(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.currencies_service = CurrencyService()

    def test_get_currencies_should_return_all(self):
        currencies = self.currencies_service.get_all()
        self.assertEqual(len(currencies), 10)

    def test_get_currencies_should_contain_cad(self):
        currencies = self.currencies_service.get_all()
        cad_currency = next((currency 
                             for currency in currencies 
                             if currency.code == 'CAD'), None)
        self.assertIsInstance(cad_currency, Currency)


if __name__ == '__main__':
    unittest.main(verbosity=2)
