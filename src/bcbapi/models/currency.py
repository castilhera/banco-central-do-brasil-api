from dataclasses import dataclass
from enum import Enum

class CurrencyType(Enum):
    A = "A"
    B = "B"

@dataclass(frozen=True)
class Currency:
    code: str
    name: str
    type: CurrencyType
