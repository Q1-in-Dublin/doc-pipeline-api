from dataclasses import dataclass
from doc_pipeline_api.errors import InvalidHoldingError


@dataclass(frozen=True)
class Holding:
    custodian : str
    isin : str
    quantity : float
    price : float
    currency : str

    @property
    def value (self) -> float:
        return self.quantity * self.price


    @classmethod #객체가 아니라 클래스에서 바로 부르는 메서드예요. 아직 객체가 없는 상태에서 "이 dict로 객체를 만들어 줘"라고 할 때 써요.
    def from_row(cls, row:dict[str,str])-> "Holding":
        try:
            quantity = float(row['quantity'])
            price = float(row["price"])

        except ValueError as e:
            raise InvalidHoldingError(f"invalid number: quantity={row['quantity']!r}, price={row['price']!r}") from e
        return cls(
            custodian=row["custodian"],
            isin = row["isin"],
            quantity = quantity,
            price = price,
            currency = row["currency"],
        )