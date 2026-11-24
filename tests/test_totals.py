import pytest

from doc_pipeline_api.totals import custodian_total

HEADER = "custodian,isin,quantity,price,currency\n"


@pytest.fixture
def make_csv(tmp_path):
    def _make(*rows: str):
        path = tmp_path / "holdings.csv"
        path.write_text(HEADER + "".join(row + "\n" for row in rows))
        return path
    return _make


def test_totals_by_custodian(make_csv):
    path = make_csv(
        "Pershing,US0378331005,100,10.0,USD",
        "Pershing,US5949181045,2,50.0,USD",
        "Citi,IE00B4L5Y983,3,20.0,EUR",
    )
    totals, skipped = custodian_total(path)
    assert totals == {"Pershing": 1100.0, "Citi": 60.0}
    assert skipped == []


def test_invalid_row_is_skipped(make_csv):
    path = make_csv(
        "Pershing,US0378331005,100,10.0,USD",
        "Citi,IE00B4L5Y983,abc,20.0,EUR",
    )
    totals, skipped = custodian_total(path)
    assert totals == {"Pershing": 1000.0}
    assert len(skipped) == 1
    assert skipped[0][0] == 3


def test_empty_file(make_csv):
    path = make_csv()
    totals, skipped = custodian_total(path)
    assert totals == {}
    assert skipped == []