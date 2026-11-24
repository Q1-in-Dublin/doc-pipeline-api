from dataclasses import dataclass

from doc_pipeline_api.errors import InvalidHoldingError


@dataclass(frozen=True)
class Holding:
    custodian: str
    isin: str
    quantity: float
    price: float
    currency: str

    @property
    def value(self) -> float:
        return self.quantity * self.price

    @classmethod
    def from_row(cls, row: dict[str, str]) -> "Holding":
        """Build a Holding from a CSV row. Raises InvalidHoldingError on bad numbers."""
        try:
            quantity = float(row["quantity"])
            price = float(row["price"])

        except ValueError as e:
            raise InvalidHoldingError(
                f"invalid number: quantity={row['quantity']!r}, price={row['price']!r}"
            ) from e
        return cls(
            custodian=row["custodian"],
            isin=row["isin"],
            quantity=quantity,
            price=price,
            currency=row["currency"],
        )
