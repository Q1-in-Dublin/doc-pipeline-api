import re

# 1. 문자열은 immutable
s = "pershing"
# s[0] = "P"           # 주석 풀고 에러 확인
t = s.upper()
print(s, t, s is t)


# 2. split, strip
raw = "  Pershing , Citi ,BNY "
print(raw.split(","))
print([x.strip() for x in raw.split(",")])

# 3. f-string 서식
amount = 1234.5
print(f"{amount:,.2f}")
print(f"{'BNY':<10}|{'Citi':>10}|")
print(f"{amount=}")

# 4. 정규식 세 가지
p = r"[A-Z]{2}"
for text in ["US123", "x US123", "US"]:
    print(text, bool(re.match(p, text)), bool(re.search(p, text)), bool(re.fullmatch(p, text)))


# ISIN 형식: 국가 코드 대문자 2자 + 대문자/숫자 9자 + 숫자 1자 = 총 12자
# 예: US0378331005 (Apple), IE00B4L5Y983
# 1) 이 형식인지 확인하는 정규식을 쓰고 re.fullmatch로 검사
pattern = r"[A-Z]{2}[A-Z0-9]{9}[0-9]"
for isin in["US0378331005", "IE00B4L5Y983", "us0378331005", "US037833100", "US0378331005X"]:
    print(isin,bool(re.fullmatch(pattern,isin)))
# 2) 아래 지저분한 줄을 깔끔한 값으로 바꾸기
line = "  Pershing , us0378331005 , 1,200 , 189.50 , usd "
parts = [x.strip() for x in line.split(",")]
print(parts)

# 결과 목표: ("Pershing", "US0378331005", 1200, 189.5, "USD")
# 힌트: 이 줄은 쉼표로 나누면 1,200의 쉼표 때문에 칸이 하나 더 생겨요. 어떻게 할지 생각해 보세요.
# 3) f-string으로 한 줄 리포트 출력
# Pershing   US0378331005    1,200 x 189.50 = 227,400.00 USD
# value = qty * price
# print(f"{Pershing}")