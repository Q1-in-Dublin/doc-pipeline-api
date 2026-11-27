from typer.testing import CliRunner

from doc_pipeline_api.cli import app

runner = CliRunner()

CSV = (
    "custodian,isin,quantity,price,currency\n"
    "Pershing,US0378331005,100,189.50,USD\n"
    "Citi,IE00B4L5Y983,10,100.00,EUR\n"
)


def test_report_writes_excel(tmp_path):
    csv_path = tmp_path / "holding.csv"
    csv_path.write_text(CSV)
    out = tmp_path / "report.xlsx"

    result = runner.invoke(app, ["report", str(csv_path), "--out", str(out)])

    assert result.exit_code == 0
    assert out.exists()
    assert "Wrote 2 holdings" in result.output


def test_report_writes_pdf(tmp_path):
    csv_path = tmp_path / "holdings.csv"
    csv_path.write_text(CSV)
    out = tmp_path / "report.pdf"

    result = runner.invoke(
        app, ["report", str(csv_path), "--out", str(out), "--format", "pdf"]
    )

    assert result.exit_code == 0
    assert out.exists()


def test_report_rejects_unknown_format(tmp_path):
    csv_path = tmp_path / "holdings.csv"
    csv_path.write_text(CSV)
    out = tmp_path / "report.csv"

    result = runner.invoke(
        app, ["report", str(csv_path), "--out", str(out), "--format", "csv"]
    )

    assert result.exit_code != 0
    assert not out.exists()
