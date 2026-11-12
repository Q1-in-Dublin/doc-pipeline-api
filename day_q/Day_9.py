# day_q/Day_9.py
def total(amounts: list[float]) -> float:
    return sum(amounts)

# print(total([1.0, 2.0]))
# print(total(["1", "2"]))     # 실행하면? mypy는?
#mypy doesn't run it just letting know the error

def find(name: str) -> str | None:
    return None

x = find("BNY")
# print(x.upper())             # 실행하면? mypy는?