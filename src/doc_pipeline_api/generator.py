import random
import string

from doc_pipeline_api.models import Holding
from doc_pipeline_api.validation import make_isin

CUSTODIANS = ["Pershing", "Citi", "BNY"]
COUNTRIES = ["US", "IE", "GB", "DE"]
CURRENCIES = ["USD", "EUR", "GBP"]


def random_isin(rng: random.Random) -> str:
    country = rng.choice(COUNTRIES)
    body = "".join(rng.choice(string.digits) for _ in range(9))

    return make_isin(country + body)


def generate_holdings(rows: int, seed: int) -> list[Holding]:

    rng = random.Random(seed)
    holdings = []

    for _ in range(rows):
        holdings.append(
            Holding(
                custodian=rng.choice(CUSTODIANS),
                isin=random_isin(rng),
                quantity=float(rng.randint(1, 1000)),
                price=round(rng.uniform(1, 500), 2),
                currency=random.choice(CURRENCIES),
            )
        )
    return holdings
