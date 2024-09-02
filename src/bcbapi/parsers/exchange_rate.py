from datetime import datetime
from bcbapi.config import Config
from bcbapi.models.exchange_rate import BulletinType, ExchangeRate

def exchange_rate_parser(obj: dict) -> ExchangeRate:
    """ Convert JSON from API to ExchangeRate """
    return ExchangeRate(
        timestamp = datetime.strptime(obj["dataHoraCotacao"],
                                      Config.RESPONSE_DATETIME_FORMAT),
        buy_parity = obj["paridadeCompra"],
        sell_parity = obj["paridadeVenda"],
        buy_quote = obj["cotacaoCompra"],
        sell_quote = obj["cotacaoVenda"],
        bulletin_type = BulletinType(obj["tipoBoletim"])
    )
