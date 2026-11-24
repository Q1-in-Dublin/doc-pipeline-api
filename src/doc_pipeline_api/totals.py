import csv
import logging
from collections import defaultdict
from pathlib import Path

from doc_pipeline_api.config import settings
from doc_pipeline_api.errors import InvalidHoldingError
from doc_pipeline_api.models import Holding

logger = logging.getLogger(__name__)


def custodian_total(path: Path) -> tuple[dict[str, float], list[tuple[int, str]]]:
    totals: defaultdict[str, float] = defaultdict(float)
    skipped: list[tuple[int, str]] = []
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        processed = 0
        for line_no, row in enumerate(reader, start=2):
            try:
                h = Holding.from_row(row)
            except InvalidHoldingError as e:
                logger.warning("Line %d skipped %s", line_no, e)
                skipped.append((line_no, str(e)))
                continue

            processed += 1

            totals[h.custodian] += h.value

        logger.info("processed %d rows, skipped %d", processed, len(skipped))
    return dict(totals), skipped


if __name__ == "__main__":
    logging.basicConfig(
        level=settings.log_level,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    )
    # p = Path(__file__).parent.parent.parent / "data" / "sample_holdings_bad.csv"
    result, skipped = custodian_total(settings.data_path)

    for name, total in result.items():
        print(f"{name:<10} {total:,.2f} ")

    if skipped:
        print(f"\nSkipped {len(skipped)} rows:")
        for line_no, reason in skipped:
            print(f"  line {line_no}: {reason}")

# Holding("Pershing", "US0378331005", "100", 189.5, "USD")
