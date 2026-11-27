from doc_pipeline_api.generator import generate_holdings
from doc_pipeline_api.models import Holding
from doc_pipeline_api.validation import is_valid_isin


def test_holdings_round_trip_through_from_row():
    for h in generate_holdings(rows=50, seed=1):
        row = {
            "custodian": h.custodian,
            "isin": h.isin,
            "quantity": str(h.quantity),
            "price": str(h.price),
            "currency": str(h.currency),
        }
        assert Holding.from_row(row) == h


def test_generates_requested_number_of_rows():
    holdings = generate_holdings(rows=50, seed=42)
    assert len(holdings) == 50


def test_same_seed_gives_same_holdings():
    holdings = generate_holdings(rows=50, seed=42)
    holdings2 = generate_holdings(rows=50, seed=42)
    assert holdings == holdings2


def test_different_seed_gives_different_holdings():
    first = generate_holdings(rows=50, seed=42)
    second = generate_holdings(rows=50, seed=41)
    assert first != second


def test_all_isins_are_valid():
    holdings = generate_holdings(rows=50, seed=42)
    assert all(is_valid_isin(h.isin) for h in holdings)
