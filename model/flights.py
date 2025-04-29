from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal


@dataclass

class Flights:
    ID: int #chiave
    AIRLINE_ID: int #chiave, serebbe ID di airline
    FLIGHT_NUMBER: int
    TAIL_NUMBER:str
    ORIGIN_AIRPORT_ID: int #chiave
    DESTINATION_AIRPORT_ID: int #chiave
    SCHEDULED_DEPARTURE_DATE:datetime.date
    DEPARTURE_DELAY: Decimal
    ELAPSED_TIME: Decimal
    DISTANCE: int
    ARRIVAL_DATE:datetime.date
    ARRIVAL_DELAY: Decimal

    # abbiamo quadrupla chiave esterna
    def __eq__(self, other):
        return (self.ID == other.ID and self.AIRLINE_ID == other.AIRLINE_ID and self.ORIGIN_AIRPORT_ID == other.ORIGIN_AIRPORT_ID and self.DESTINATION_AIRPORT_ID == other.DESTINATION_AIRPORT_ID)

    def __hash__(self):
        return hash(self.ID, self.AIRLINE_ID, self.ORIGIN_AIRPORT_ID, self.DESTINATION_AIRPORT_ID)

    def __str__(self):
        return (f"Volo:{self.ID}; Numero: {self.FLIGHT_NUMBER}; Partenza:{self.ORIGIN_AIRPORT_ID}; Destinazione:{self.DESTINATION_AIRPORT_ID}")


