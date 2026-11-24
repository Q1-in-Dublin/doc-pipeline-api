import re

ISIN_PATTERN = re.compile(r"[A-Z]{2}[A-Z0-9]{9}[0-9]")


def is_valid_isin(isin: str) -> bool:
    if not ISIN_PATTERN.fullmatch(isin):
        return False

    digits = "".join(str(int(c, 36)) for c in isin)
    total = 0

    for i, ch in enumerate(reversed(digits)):
        n = int(ch)
        if i % 2 == 1:
            n = n * 2
            if n > 9:
                n -= 9
        total += n
    return total % 10 == 0
