1.s = "pershing"일 때 s[0] = "P"는 왜 에러가 날까요? 그럼 s.upper()는 s를 바꾸나요?
String은 Immutable이라서 바꿀수없다. => 결국 hashable하다. dictionary사용가능하다 2. 루프에서 result += piece로 문자열을 계속 붙이면 왜 느릴 수 있고, 대신 무엇을 쓰나요?
+=이거는 새로운 문자열을 만들기때문에 속도가 기존문자열 + 복사문자열 O(n^2) 대신에 Join을쓴다.Join은 O(n)이다.
3." Pershing , Citi ,BNY ".split(",")의 결과는? 공백까지 깔끔하게 하려면?
일단 [" Pershing "," Citi ", " BNY ", ]
그러면 " Pershing , Citi ,BNY ".split(",").strip()
raw =" Pershing , Citi ,BNY "
[x.strip() for x in raw.split(",")]
4.f-string에서 f"{1234.5:,.2f}", f"{'BNY':<10}|", f"{amount=}"는 각각 뭘 출력하나요?

5.정규식에서 re.match, re.search, re.fullmatch의 차이는? 패턴 앞에 r"..."을 붙이는 이유는?
=> re.match -> 맨 앞자리부터 시작
=> re.search -> 어디든 패턴이 있으면
=> Re.fullmatch: 처음부터 끝까지 같아야함
r"..."을 붙이는 이유정규식은 \d(숫자), \s(공백), \b(단어 경계)처럼 역슬래시를 많이 써요. 그런데 일반 파이썬 문자열에서도 역슬래시는 특별한 뜻이 있어요(\n 줄바꿈, \t 탭, \b 백스페이스). 그래서 정규식에 닿기 전에 파이썬이 먼저 바꿔 버릴 수 있어요.
print(len("\b")) # 1 ← 파이썬이 백스페이스 문자 하나로 바꿈
print(len(r"\b")) # 2 ← 역슬래시와 b 그대로
