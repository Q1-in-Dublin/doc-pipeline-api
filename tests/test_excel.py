import pytest
from openpyxl import load_workbook

from doc_pipeline_api.excel import HEADER, write_holdings_excel
from doc_pipeline_api.models import Holding


def make_holdings() -> list[Holding]:
    return [
        Holding("Pershing", "US0378331005", 100.0, 189.5, "USD"),
        Holding("Pershing", "US5949181045", 40.0, 415.2, "USD"),
        Holding("Citi", "IE00B4L5Y983", 10.0, 100.0, "EUR"),
    ]


def test_creates_summary_and_custodian_sheets(tmp_path):
    path = tmp_path / "holdings.xlsx"
    write_holdings_excel(make_holdings(), path)

    wb = load_workbook(path)
    assert wb.sheetnames == ["summary", "Pershing", "Citi"]


def test_summary_has_total_per_custodian(tmp_path):
    path = tmp_path / "holdings.xlsx"
    write_holdings_excel(make_holdings(), path)

    rows = list(load_workbook(path)["summary"].iter_rows(values_only=True))

    print(rows)
    assert rows[0] == ("custodian", "total_value")
    assert rows[1][0] == "Pershing"
    assert rows[1][1] == pytest.approx(100 * 189.5 + 40 * 415.2)
    assert rows[2] == ("Citi", 10 * 100)


def test_custodian_sheet_has_header_and_rows(tmp_path):
    path = tmp_path / "holdings.xlsx"
    write_holdings_excel(make_holdings(), path)

    rows = list(load_workbook(path)["Pershing"].iter_rows(values_only=True))
    assert len(rows) == 3
    assert rows[0] == tuple(HEADER)
    assert rows[1] == ("Pershing", "US0378331005", 100.0, 189.5, "USD", 100 * 189.5)
