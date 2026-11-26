from collections import defaultdict
from pathlib import Path

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table

from doc_pipeline_api.models import Holding

TABLE_HEADER = ["ISIN", "Quantity", "Price", "Currency", "Value"]


def write_holdings_pdf(holdings: list[Holding], path: Path) -> None:
    """Write a holdings report PDF: one section per custodian with a table and total."""

    by_custodian: defaultdict[str, list[Holding]] = defaultdict(list)
    for h in holdings:
        by_custodian[h.custodian].append(h)

    styles = getSampleStyleSheet()
    story = [Paragraph("Custodian Holdings Report", styles["Title"])]

    for custodian, items in by_custodian.items():
        story.append(Paragraph(custodian, styles["Heading2"]))

        rows = [TABLE_HEADER]
        for h in items:
            rows.append([h.isin, h.quantity, h.price, h.currency, h.value])

        story.append(Table(rows))
        total = sum(h.price * h.quantity for h in items)
        story.append(Paragraph(f"Total: {total:,.2f}", styles["Normal"]))
        story.append(Spacer(1, 12))

    SimpleDocTemplate(str(path), pagesize=A4).build(story)
