from dataclasses import dataclass
from decimal import Decimal


@dataclass

class Airports:
    ID: int #chiave
    IATA_CODE:str
    AIRPORT:str
    CITY:str
    STATE:str
    COUNTRY:str
    LATITUDE:Decimal
    LONGITUDE:Decimal
    TIMEZONE_OFFSET:Decimal

    def __eq__(self, other):
        return self.ID == other.ID

    def __hash__(self):
        return hash(self.ID)

    def __str__(self):
        return f"Aereoporto:{self.ID}"