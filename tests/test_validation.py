import pytest

from doc_pipeline_api.validation import is_valid_isin, make_isin


@pytest.mark.parametrize(
    "isin",
    [
        "US0378331005",
        "US5949181045",
        "US0231351067",
        "US88160R1014",
        "IE00B4L5Y983",
        "IE00B5BMR087",
        "DE0007164600",
        "GB0002634946",
        "IE00BK5BQT80",
        "US02079K3059",
    ],
)
def test_valid_isins(isin):
    assert is_valid_isin(isin)


@pytest.mark.parametrize(
    "isin",
    [
        "US0378331006",
        "us0378331005",
        "US037833100",
        "US03783310055",
        "US03783310-5",
        "",
        "1S0378331005",
    ],
    ids=[
        "wrong_check_digit",
        "lowercase",
        "too_short",
        "too_long",
        "special_char",
        "empty",
        "digit_in_country_code",
    ],
)
def test_invalid_isins(isin):
    assert not is_valid_isin(isin)


# def test_valid_isin():
#     assert is_valid_isin("US0378331005")

# def test_wrong_check_digit():
#     assert not is_valid_isin("US0378331006")


# def test_lowercase_is_invalid():
#     assert not is_valid_isin("us0378331005")
@pytest.mark.parametrize(
    ("base11", "expected"),
    [("US037833100", "US0378331005"), ("IE00B4L5Y98", "IE00B4L5Y983")],
)
def test_make_isin_adds_correct_check_digit(base11, expected):
    assert make_isin(base11) == expected
