from dataclasses import dataclass
from datetime import datetime
from enum import Enum

class BulletinType(Enum):
    Opening = "Abertura"
    Intermediate = "Intermediário"
    Closing = "Fechamento"
    ClosingPTAX = "Fechamento PTAX"

@dataclass(frozen=True)
class ExchangeRate:
    timestamp: datetime
    buy_parity: float
    sell_parity: float
    buy_quote: float
    sell_quote: float
    buy_parity: float
    bulletin_type: BulletinType
