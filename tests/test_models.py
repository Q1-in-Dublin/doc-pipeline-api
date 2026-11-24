import dataclasses

import pytest

from doc_pipeline_api.errors import InvalidHoldingError
from doc_pipeline_api.models import Holding


def make_row(**overrides: str) -> dict[str, str]:
    row = {
        "custodian": "Pershing",
        "isin": "US0378331005",
        "quantity": "100",
        "price": "189.50",
        "currency": "USD",
    }
    unknown = set(overrides) - set(row)
    assert not unknown, f"unknown columns: {unknown}"
    row.update(overrides)
    return row


def test_value_is_quantity_times_price():
    h = Holding.from_row(make_row())
    assert h.value == pytest.approx(18950.0)


def test_holding_is_frozen():
    h = Holding.from_row(make_row())
    with pytest.raises(dataclasses.FrozenInstanceError):
        h.price = 200.0


def test_invalid_quantity_raises():
    with pytest.raises(InvalidHoldingError):
        Holding.from_row(make_row(quantity="abc"))


def test_empty_price_raises():
    with pytest.raises(InvalidHoldingError):
        Holding.from_row(make_row(price=""))


def test_error_keeps_original_cause():
    with pytest.raises(InvalidHoldingError) as exc_info:
        Holding.from_row(make_row(quantity="abc"))
    assert isinstance(exc_info.value.__cause__, ValueError)


def test_error_message_includes_bad_value():
    with pytest.raises(InvalidHoldingError, match="quantity='abc'"):
        Holding.from_row(make_row(quantity="abc"))


def test_quantity_with_spaces_is_parsed():
    h = Holding.from_row(make_row(quantity=" 100 "))
    assert h.quantity == 100


def test_quantity_with_thousands_separator_raises():
    with pytest.raises(InvalidHoldingError):
        Holding.from_row(make_row(quantity="100,000"))


@pytest.mark.xfail(reason="TODO: from_row should reject nan/inf")
@pytest.mark.parametrize("bad", ["nan", "inf"])
def test_nan_quantity_raises(bad):
    with pytest.raises(InvalidHoldingError):
        Holding.from_row(make_row(quantity=bad))


def test_negative_quantity_is_accepted():
    h = Holding.from_row(make_row(quantity="-50"))
    assert h.quantity == -50


@pytest.mark.xfail(
    reason="TODO: missing column raises KeyError, should be InvalidHoldingError"
)
def test_missing_column_raises_invalid_holding():
    row = make_row()
    del row["price"]
    with pytest.raises(InvalidHoldingError):
        Holding.from_row(row)


@pytest.mark.xfail(reason="TODO: from_row should validate ISIN with is_valid_isin")
def test_invalid_isin_raises():
    with pytest.raises(InvalidHoldingError):
        Holding.from_row(make_row(isin="NOT_AN_ISIN"))


def test_from_row_parses_valid_row():
    h = Holding.from_row(make_row())
    assert h.custodian == "Pershing"
    assert h.quantity == 100.0
    assert h.price == 189.5


def test_invalid_price_raises():
    with pytest.raises(InvalidHoldingError):
        Holding.from_row(make_row(price="abc"))
