# 1. 없는 키
# d = {"a": 1}
# print(d.get("x"), d.get("x", 0))
# print(d["x"])   # 주석 풀고 에러 확인
# d.get("x") # KeyError
# d.get("x", 0) # 0
# print(d["x"]) 

# 2. list vs set 검색 속도
# import time
# n = 1_000_000
# nums_list = list(range(n))
# nums_set = set(nums_list)
# for name, c in [("list", nums_list), ("set", nums_set)]:
#     t = time.perf_counter()
#     for _ in range(100):
#         (n - 1) in c
#     print(name, round(time.perf_counter() - t, 4))

# 3. defaultdict 없이 vs 있게: 단어를 첫 글자로 묶기
from collections import defaultdict
words = ["apple", "avocado", "banana", "blueberry", "cherry"]
# print(dict(words))
# 일반 dict로 먼저 짜 보고, defaultdict(list)로 다시 짜기
print(defaultdict(list))

# groups = {}
# for w in words:
#     first = w[0]
#     if first not in groups:
#         groups[first] = []
#     groups[first].append(w)
# print(groups)

groups = defaultdict(list)
for w in words:
    groups[w[0]].append(w)


# 4. Counter
# from collections import Counter
# c = Counter("mississippi")
# print(c, c["s"], c["z"], c.most_common(2))

rows = [
    ("Pershing", 1000.0),
    ("Citi", 250.5),
    ("Pershing", 300.0),
    ("Citi", 49.5),
    ("BNY", 700.0),
]

# totals = {}
# for name, amount in rows:
#     totals[name] = totals.get(name,0) + amount
# print(totals)

totals = defaultdict(float)

for name, amount in rows:
    totals[name] = totals[name] + amount
print(totals)