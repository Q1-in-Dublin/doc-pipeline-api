from pypdf import PdfReader

from doc_pipeline_api.models import Holding
from doc_pipeline_api.pdf import write_holdings_pdf


def make_holdings() -> list[Holding]:
    return [
        Holding("Pershing", "US0378331005", 100.0, 189.5, "USD"),
        Holding("Pershing", "US5949181045", 40.0, 415.2, "USD"),
        Holding("Citi", "IE00B4L5Y983", 10.0, 100.0, "EUR"),
    ]


def test_pdf_has_title(tmp_path):
    path = tmp_path / "report.pdf"
    write_holdings_pdf(make_holdings(), path)

    reader = PdfReader(path)
    text = "".join(page.extract_text() for page in reader.pages)
    assert "Custodian Holdings Report" in text


def test_pdf_has_each_custodian(tmp_path):
    path = tmp_path / "report.pdf"
    write_holdings_pdf(make_holdings(), path)

    reader = PdfReader(path)
    text = "".join(page.extract_text() for page in reader.pages)
    assert "Pershing" in text
    assert "Citi" in text


def test_pdf_has_total_per_custodian(tmp_path):
    path = tmp_path / "report.pdf"
    write_holdings_pdf(make_holdings(), path)

    reader = PdfReader(path)
    text = "".join(page.extract_text() for page in reader.pages)
    assert "Total: 35,558.00" in text
    assert "Total: 1,000.00" in text
