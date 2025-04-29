from dataclasses import dataclass


@dataclass
#compagnia aerea
class Airlines:
    ID: int #chiave
    IATA_CODE:str
    AIRLINE:str

    def __eq__(self, other):
        return self.ID == other.ID

    def __hash__(self):
        return hash(self.ID)

    def __str__(self):
        return f"Compagnia aerea:{self.ID}"