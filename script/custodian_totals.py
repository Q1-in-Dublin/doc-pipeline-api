import csv
from collections import defaultdict
from pathlib import Path

from doc_pipeline.errors import InvalidHoldingError
from doc_pipeline.models import Holding

def custodian_total(path):
    totals = defaultdict(float)

    with open(path, newline="") as f:
        reader = csv.DictReader(f)

        for row in reader:
            custodian = row['custodian']
            quantity = float(row['quantity'])
            price = float(row['price'])
            value = quantity * price
            totals[custodian] += value





    return dict(totals)
if __name__ == "__main__":
    p = Path(__file__).parent.parent / "data" / "sample_holdings.csv"
    result = custodian_total(p)

    for name, total in result.items():
        print(f"{name:<10} {total:,.2f} ")



