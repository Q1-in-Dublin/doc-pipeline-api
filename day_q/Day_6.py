from dataclasses import dataclass

# 1. 일반 클래스
class HoldingPlain:
    def __init__(self, custodian, isin, quantity, price):
        self.custodian = custodian
        self.isin = isin
        self.quantity = quantity
        self.price = price

a = HoldingPlain("Pershing", "US0378331005", 100, 189.5)
b = HoldingPlain("Pershing", "US0378331005", 100, 189.5)
#print(a)          # 어떻게 나오나? => obejct address
#print(a == b)     # True? False? =>false

# 2. dataclass
@dataclass
class Holding:
    custodian: str
    isin: str
    quantity: float
    price: float

c = Holding("Pershing", "US0378331005", 100, 189.5)
d = Holding("Pershing", "US0378331005", 100, 189.5)
# print(c)          # 일반 클래스와 비교
# print(c == d)

# 3. frozen
@dataclass(frozen=True)
class FrozenHolding:
    isin: str
    quantity: float

f = FrozenHolding("US0378331005", 100)
# f.quantity = 200      # 주석 풀고 에러 확인
#print(hash(f))           # Holding으로도 hash()를 해 보고 차이 확인