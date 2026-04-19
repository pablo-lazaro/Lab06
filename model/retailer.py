from dataclasses import dataclass

@dataclass

class Retailer:
    code: str
    name: str
    type: str
    country: str

    def __eq__(self, other):
        return self.code == other.code  # codins perche questo metodo paragona solo le chiavi primarie

    def __hash__(self):
        return hash(self.code)  # DI nuovo, chiave primaria per il metodo hash

    def __str__(self):  # questa è la stampa
        return f"{self.name}"