from datetime import datetime
from bcbapi.config import Config
from bcbapi.models.ptax import PTAX

def ptax_parser(obj: dict) -> PTAX:
    """ Convert JSON from API to PTAX """
    return PTAX(
        timestamp = datetime.strptime(obj["dataHoraCotacao"],
                                      Config.RESPONSE_DATETIME_FORMAT),
        buy = obj["cotacaoCompra"],
        sell = obj["cotacaoVenda"]
    )
