import csv
import logging
from pathlib import Path
from typing import Annotated

import typer

from doc_pipeline_api.errors import InvalidHoldingError
from doc_pipeline_api.excel import write_holdings_excel
from doc_pipeline_api.models import Holding
from doc_pipeline_api.pdf import write_holdings_pdf

app = typer.Typer()


@app.callback()
def main() -> None:
    """Document pipeline tools."""


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

    if fmt == "excel":
        write_holdings_excel(holdings, out)
    elif fmt == "pdf":
        write_holdings_pdf(holdings, out)
    else:
        raise typer.BadParameter(f"{fmt} is wrong, choose between excel and pdf")
    typer.echo(f"Wrote {len(holdings)} holdings to {out}")
