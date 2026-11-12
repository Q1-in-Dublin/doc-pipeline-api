import csv
from pathlib import Path
from collections import defaultdict
from doc_pipeline_api.errors import InvalidHoldingError  
from doc_pipeline_api.models import Holding

def custodian_total(path:Path) -> tuple[dict[str,float],list[tuple[int,str]]]:
    totals : defaultdict[str,float] = defaultdict(float) 
    skipped : list[tuple[int,str]] = []
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
    p = Path(__file__).parent.parent.parent / "data" / "sample_holdings_bad.csv"
    result,skipped = custodian_total(p)

    for name, total in result.items():
        print(f"{name:<10} {total:,.2f} ")

    if skipped :
        print(f"\nSkipped {len(skipped)} rows:")
        for line_no, reason in skipped:
            print(f"  line {line_no}: {reason}")

Holding("Pershing", "US0378331005", "100", 189.5, "USD")