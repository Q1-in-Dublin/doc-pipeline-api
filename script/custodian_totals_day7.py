import csv
from pathlib import Path
from collections import defaultdict
from dataclasses import dataclass

class InvalidHoldingError(ValueError):
    pass

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
    def from_row(cls, row:dict)->"Holding":
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
def custodian_total(path):
    totals = defaultdict(float)
    skipped = []
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        for line_no, row in enumerate(reader, start=2):
            try:
                h =Holding.from_row(row)
            except InvalidHoldingError as e:
                skipped.append((line_no,str(e)))
            continue
        totals[h.custodian] += h.value
            
            
    return dict(totals), skipped

if __name__ == "__main__":
    p = Path(__file__).parent.parent / "data" / "sample_holdings_bad.csv"
    result,skipped = custodian_total(p)

    for name, total in result.items():
        print(f"{name:<10} {total:,.2f} ")

    if skipped :
        print(f"\nSkipped {len(skipped)} rows:")
        for line_no, reason in skipped:
            print(f"  line {line_no}: {reason}")



