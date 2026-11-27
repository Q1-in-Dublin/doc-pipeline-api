import math
from dataclasses import dataclass

from doc_pipeline_api.errors import InvalidHoldingError
from doc_pipeline_api.validation import is_valid_isin


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
        """Build a Holding from a CSV row.
        Raises InvalidHoldingError on invalid or missing values.
        """
        isin = row.get("isin", "")
        if not is_valid_isin(isin):
            raise InvalidHoldingError(f"Invalid isin ={row['isin']!r}")
        try:
            quantity = float(row["quantity"])
            price = float(row["price"])

        except (ValueError, KeyError) as e:
            raise InvalidHoldingError(
                f"invalid number: quantity={row.get('quantity')!r}, "
                f"price={row.get('price')!r}"
            ) from e

        if not math.isfinite(quantity) or not math.isfinite(price):
            raise InvalidHoldingError(
                f"non-finite number: quantity={row['quantity']!r}, "
                f"price={row['price']!r}"
            )

        return cls(
            custodian=row["custodian"],
            isin=row["isin"],
            quantity=quantity,
            price=price,
            currency=row["currency"],
        )
