from dataclasses import dataclass

@dataclass
class Vendita:
    data: str
    brand: str
    retailer_code: int
    ricavo: float

    def __str__(self):
        return f"Data: {self.data} | Brand: {self.brand} | Retailer: {self.retailer_code} | Ricavo: {self.ricavo:.2f}"