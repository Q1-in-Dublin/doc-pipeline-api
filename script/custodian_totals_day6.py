import csv
from pathlib import Path
from collections import defaultdict
from dataclasses import dataclass

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
        return cls(
            custodian=row["custodian"],
            isin = row["isin"],
            quantity = float(row["quantity"]),
            price = float(row["price"]),
            currency = row["currency"],
        )
    
def custodian_total(path):
    totals = defaultdict(float)

    with open(path, newline="") as f:
        reader = csv.DictReader(f)

        for row in reader:
            h =Holding.from_row(row)
            totals[h.custodian] += h.value

    return dict(totals)
if __name__ == "__main__":
    p = Path(__file__).parent.parent / "data" / "sample_holdings.csv"
    result = custodian_total(p)

    for name, total in result.items():
        print(f"{name:<10} {total:,.2f} ")



