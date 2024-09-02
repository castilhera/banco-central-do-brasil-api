from bcbapi.models.currency import Currency, CurrencyType

def currency_parser(obj: dict) -> Currency:
    """ Convert JSON from API to Currency """
    return Currency(
        code=obj["simbolo"],
        name=obj["nomeFormatado"],
        type=CurrencyType[obj["tipoMoeda"]]
    )
