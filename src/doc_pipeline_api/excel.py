from collections import defaultdict
from pathlib import Path

from openpyxl import Workbook

from doc_pipeline_api.models import Holding

HEADER = ["custodian", "isin", "quantity", "price", "currency", "value"]


def write_holdings_excel(holdings: list[Holding], path: Path) -> None:
    """Write holdings to an Excel file: one sheet per custodian and a Summary sheet."""
    by_custodian: defaultdict[str, list[Holding]] = defaultdict(list)

    for h in holdings:
        by_custodian[h.custodian].append(h)

    wb = Workbook()
    summary = wb.active
    summary.title = "summary"
    summary.append(["custodian", "total_value"])

    for custodian, items in by_custodian.items():
        # custodian sheet
        ws = wb.create_sheet(custodian)
        ws.append(HEADER)

        for h in items:
            ws.append([h.custodian, h.isin, h.quantity, h.price, h.currency, h.value])
        summary.append([custodian, sum(h.value for h in items)])

    wb.save(path)
