from dataclasses import dataclass
from datetime import datetime

@dataclass(frozen=True)
class PTAX:
    timestamp: datetime
    buy: float
    sell: float