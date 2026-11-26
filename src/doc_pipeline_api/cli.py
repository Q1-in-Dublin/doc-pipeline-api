import csv
import logging
from pathlib import Path
from typing import Annotated

import typer

from doc_pipeline_api.errors import InvalidHoldingError
from doc_pipeline_api.models import Holding

app = typer.Typer()
logger = logging.getLogger(__name__)


@app.command()
def report(
    csv_path: Annotated[Path, typer.Argument(exists=True)],
    out: Annotated[Path, typer.Option("--out")],
    fmt: Annotated[str, typer.Option("--format")] = "excel",
) -> None:

    holdings: list[Holding] = []

    with open(csv_path, newline="") as f:
        for line_no, row in enumerate(csv.DictReader(f), start=2):
            try:
                h = Holding.from_row(row)

            except InvalidHoldingError as e:
                logger.warning("line %d skipped: %s", line_no, e)
                continue
            holdings.append(h)
