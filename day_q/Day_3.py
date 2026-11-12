# 1. keyword-only
def total(amounts, *, currency="EUR"):
    return f"{sum(amounts)} {currency}"
print(total([1, 2], currency="USD"))
# print(total([1, 2], "USD"))   # 주석 풀고 에러 확인

# 2. *args, **kwargs
def show(*args, **kwargs):
    print(type(args), args) # 1,2 <Tuple>
    print(type(kwargs), kwargs) # name ='Pershing' , amount = 100 < Dictionary>
# show(1, 2, name="Pershing", amount=100)

nums = [3, 1, 2]
print(max(*nums))          # max(3, 1, 2)와 같음
info = {"sep": " | "}
print("a", "b", **info)    # print("a", "b", sep=" | ")와 같음

# # 3, 4. 스코프
def outer():
    cnt = 0
    grid = ["1"]
    def inner():
        grid[0] = "0"   # 되는 이유? : 그냥 값만 바꿔주는거라 assgin 아니고
        # cnt += 1      # 주석 풀고 에러 확인, 그다음 nonlocal로 고치기 : 이건 Cnt +1 이므로 변수가 바뀜 로컬변수처리됨
    inner()
    print(cnt, grid)
outer()

from collections import defaultdict
rows = [
    ("Pershing", 1000.0),
    ("Citi", 250.5),
    ("Pershing", 300.0),
    ("Citi", 49.5),
    ("BNY", 700.0),
]

def sum_by_custodian(rows, *, min_amount=0.0):
    # min_amount보다 작은 금액은 건너뛰고
    totals = defaultdict(float)  
    for name, amount in rows:
        if amount < min_amount :
            continue
        totals[name] += amount
    return dict(totals)

    # 커스터디언별 합계를 dict로 return
    ...

print(sum_by_custodian(rows))
# {'Pershing': 1300.0, 'Citi': 300.0, 'BNY': 700.0}
print(sum_by_custodian(rows, min_amount=100))
# {'Pershing': 1300.0, 'Citi': 250.5, 'BNY': 700.0}