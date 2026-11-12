## 2026-11-02 (Day 1): list, tuple, 슬라이싱, comprehension

### 아침: Group Anagrams

- 패턴: 해시맵. 정렬한 문자열을 키로 defaultdict(list)에 단어를 모음

### 함수 기본 인자에 list를 쓰면

- `def add(item, bucket=[])`는 호출할 때마다 값이 누적됨
- 기본값은 함수 정의 시점에 한 번만 만들어지고 모든 호출이 같은 객체를 공유
- 해결: 기본값을 None으로 두고 함수 안에서 새로 만듦
  `if bucket is None: bucket = []`

### 복사: =, [:], deepcopy

- `b = a`: 같은 객체를 가리킴 (복사 아님)
- `b = a[:]`: 얕은 복사. 바깥 리스트만 새것, 안의 원소는 같은 객체 공유
- `copy.deepcopy(a)`: 안쪽까지 전부 새로 만듦
- 안에 mutable(리스트 안의 리스트)이 있을 때만 차이가 드러남
- `id()`로 주소 확인, `is`는 같은 객체인지, `==`는 값이 같은지

### hashable

- hash 값을 만들 수 있고, 그 값이 평생 바뀌지 않는 객체
- dict는 hash 값을 서랍 번호처럼 써서 바로 찾음 → 그래서 키가 바뀌면 못 찾음
- int, str, tuple은 hashable / list, dict, set은 아님
- immutable ≠ hashable: tuple은 immutable이지만 `([1], 2)`처럼 안에 list가 있으면 unhashable
- 그래서 dict 키의 조건은 immutable이 아니라 hashable

### list comprehension vs generator expression

- `[x for x in ...]`: 모든 값을 즉시 만들어 메모리에 저장 → O(n) 메모리
- `(x for x in ...)`: 꺼낼 때마다 하나씩 만듦 → 메모리 거의 안 씀
- generator는 한 번만 순회 가능, 인덱스 접근 불가
- 한 번 흘려보낼 때(sum, max, 파일 한 줄씩)는 generator

### 슬라이싱

- 새 리스트를 만드는 얕은 복사, 길이 k만큼 복사하므로 O(k)
- 루프에서 매번 `s[1:]` → O(n) 같지만 실제로는 O(n²)
- 해결: 복사 대신 인덱스를 옮김
- 뒤집기 세 가지: `[::-1]`(새 리스트), `.reverse()`(원본 변경, None 반환), `reversed()`(반복자)

### comprehension 연습

- 평탄화: `[x for inner in nested for x in inner]` (for문 순서 그대로)
- 조건: `[i**2 for i in range(10) if i % 2 == 0]`
- dict: `{fruit: len(fruit) for fruit in fruits}`

### 오늘 걸린 실수

- `^`는 제곱이 아니라 XOR → 제곱은 `**`
- `//`는 몫, `%`는 나머지 → 짝수 판별은 `i % 2 == 0`
- 변수 이름을 `list`로 쓰면 내장 함수 list()를 덮어씀

## 2026-11-03 (Day 2): dict, set, Counter, defaultdict

### 아침: Longest Substring Without Repeating Characters

- 브루트포스: 시작점마다 오른쪽으로 가며 set으로 중복 확인 → O(n²)
- 최적화: 슬라이딩 윈도우. right는 한 칸씩 전진, 중복이면 while로 left 쪽 글자를 빼며 당김 → O(n)
- 실수: 중복일 때 `if`로 한 번만 뺌 → `while`이어야 함. 빼는 글자는 s[right]가 아니라 s[left]
- 투 포인터 두 종류: 양끝에서 가운데로(팰린드롬) vs 같은 방향으로(슬라이딩 윈도우)

### d["x"] vs d.get("x")

- 키가 없으면 `d["x"]`는 KeyError, `d.get("x")`는 None
- `d.get("x", 0)`처럼 기본값을 줄 수 있음

### list vs set 검색

- `x in list`는 처음부터 하나씩 비교 → O(n)
- `x in set`은 hash로 위치를 바로 찾음 → 평균 O(1)

### hashable이 dict 키와 set 원소에 필요한 이유

- 둘 다 hash 값으로 저장 위치를 정하고, 같은 hash로 다시 찾음
- hash가 바뀌면 못 찾으니 hash가 평생 고정된 객체만 가능
- set = 값 없이 키만 있는 dict

### defaultdict

- 인덱스와는 상관없음. dict와 똑같이 키로 접근
- 차이는 없는 키에 접근할 때 지정한 기본값을 자동으로 만들어 줌
- 괄호 안 = 시작 값의 종류: 모으기 list([]), 세기 int(0), 금액 더하기 float(0.0)

### Counter

- 개수 세기에 특화된 dict (dict를 상속)
- 없는 키는 KeyError 없이 0
- `most_common(n)` → 많은 순서로 (원소, 개수) 튜플 리스트

### 오늘 걸린 에러

- `dict(words)` → ValueError: dict()는 (키, 값) 쌍 리스트만 받음
- `dict(rows)` → 에러는 없지만 같은 키는 덮어써서 합계가 틀림 (에러보다 위험)
- `totals[name] += amount` (일반 dict) → KeyError: 읽을 값이 없음
- `defaultdict(list)`에 숫자 더하기 → TypeError: [] + float 불가
- 리스트를 문자열로 인덱싱 `words["a"]` → TypeError

### 커스터디언별 합계 (금요일 과제 연습)

- 일반 dict: `totals[name] = totals.get(name, 0) + amount`
- defaultdict: `totals = defaultdict(float)` 후 `totals[name] += amount`

## 2026-11-04 (Day 3): 함수, 인자, \*args·\*\*kwargs, 스코프

### 아침: Number of Islands

- 격자를 이중 for문으로 훑다가 "1"을 만나면 cnt+1, dfs로 붙은 땅을 전부 "0"으로 지움
- "0"으로 바꾸기 = 방문 표시. 무한 재귀와 중복 카운트를 막음. 이웃 호출 전에 바꿔야 함
- 범위 조건은 >= rows, >= cols. 범위 확인을 grid[r][c] 읽기보다 먼저 (or는 앞에서 참이면 멈춤)
- 값은 문자열 "1", "0"
- 시간 O(m·n), 공간 O(m·n) (재귀 스택). 큰 격자는 RecursionError 위험 → BFS(deque)로

### keyword-only 인자

- def f(a, _, c): _ 뒤는 c=3처럼 이름을 붙여서만 넘길 수 있음
- 옵션 값을 위치로 잘못 넘기는 실수를 막음
- parameter = 정의의 이름, argument = 호출할 때 넘기는 값

### \*args, \*\*kwargs

- 정의: \*args는 위치 인자를 tuple로, \*\*kwargs는 키워드 인자를 dict로 모아서 받음
- 호출: f(\*list)는 풀어서 위치 인자로, f(\*\*dict)는 풀어서 키워드 인자로
- 정의에서는 모으고, 호출에서는 푼다

### 스코프와 LEGB

- 찾는 순서: Local → Enclosing → Global → Built-in
- 함수 안에서 대입(=, +=)하면 그 변수는 함수 전체에서 Local
- count += 1 → 지역 변수인데 값이 없어 UnboundLocalError
- 바깥을 바꾸려면 global(전역), nonlocal(감싸는 함수). 실무에선 인자와 return 선호
- grid[r][c] = "0"은 grid를 읽고 안쪽만 바꿈(rebind 아님) → 바깥에 반영
- cnt += 1은 cnt 이름을 다시 묶음(rebind) → 지역 변수
- 내장 이름(list)으로 변수를 만들면 Built-in이 가려짐
- 감싸는 함수의 변수를 쓰는 안쪽 함수 = closure (dfs)

### sum_by_custodian

- defaultdict(float)로 합계, 작은 금액은 continue
- 밖으로 내보낼 땐 dict(totals): 없는 키 조회가 조용히 0.0이 되는 걸 막음
- return 뒤 코드는 실행되지 않음(dead code)

## 1주차 회고 (11/2 ~ 11/8)

### 지킨 시간

| 요일 | 아침 알고리즘                          | 저녁 부트캠프                                        |
| ---- | -------------------------------------- | ---------------------------------------------------- |
| 월   | ✅ Group Anagrams                      | ✅ list, tuple, 슬라이싱, comprehension              |
| 화   | ✅ Longest Substring (최적해는 저녁에) | ✅ dict, set, Counter, defaultdict (21:30 늦게 시작) |
| 수   | ✅ Number of Islands (저녁에 함)       | ✅ 함수, \*args, \*\*kwargs, 스코프                  |
| 목   | ✅ Level Order Traversal               | ✅ 문자열, f-string, 정규식                          |
| 금   | ❌ → 일요일에 Merge Intervals          | ❌ → 일요일에 CSV 합계 과제                          |
| 일   | ✅ Kth Largest, 복습 3문제             | ✅ CSV 과제 (PR은 생략)                              |

- 저녁 주제 5개 모두 끝냄, 금요일 과제도 일요일에 따라잡음
- 아침 시간대는 잘 안 지켜짐: 수요일 문제를 저녁에 풀었음
- 진단 7문제 중 6개 완료 (Search in Rotated Sorted Array 남음)

### 가장 많이 막힌 곳

- **무엇으로 꺼내는지 헷갈림**: 리스트에 문자열 인덱스(`words[first]`, `strs[key]`), 이미 꺼낸 값을 다시 키로 씀(`row[custodian]`)
- **= 와 += 와 ==**: 합계에서 `=`로 덮어씀(dict(rows), totals[custodian] = value, result[key] = word), 대입 자리에 `==`
- **경계 조건**: 격자 범위에서 `>`와 `>=`, 음수 인덱스 빠뜨림
- **타입 확인 없이 메서드 체이닝**: `split().strip()`, `deque(root)`, `heappush(heap, nums)`
- 새 개념(hashable, generator, LEGB, 정규식)은 설명 들으면 이해됐음

### 다음 주에 바꿀 것 하나

- 코드가 이상하면 고치기 전에 `print(type(x), x)`로 **지금 이 변수가 뭔지** 먼저 확인하기

### 다음 주 아침 우선순위

- 월: Search in Rotated Sorted Array (남은 진단)
- 그다음: 힌트를 많이 받은 패턴부터 (슬라이딩 윈도우, 구간)

## 2026-11-09 (2주차 월): 클래스와 dataclass

### 아침: Search in Rotated Sorted Array

- 브루트포스: enumerate로 순회하며 값 비교 → O(n), 공간 O(1)
- enumerate는 항상 (인덱스, 값) 순서. 변수 이름을 내용에 맞게 (i, num)
- hash로 찾기는 dict를 만드는 데 O(n) + 공간 O(n) → 한 번만 찾을 땐 손해. 여러 번 찾을 때만 이득
- 최적화: 이진 탐색 → O(log n)
    - 가운데로 자르면 둘 중 한쪽은 반드시 정렬돼 있음 (꺾이는 지점은 한 곳뿐)
    - nums[left] <= nums[mid]면 왼쪽 정렬 → target이 nums[left] <= target < nums[mid]면 왼쪽으로
    - 아니면 오른쪽 정렬 → nums[mid] < target <= nums[right]면 오른쪽으로
- 기본 이진 탐색: while left <= right, mid = (left+right)//2, mid ± 1로 좁힘
- 실수: 오른쪽 조건에 nums[left]를 씀 (정렬 안 된 쪽 값), num[right] 오타

### class와 객체

- class는 설계도(blueprint), 객체(인스턴스)는 그걸로 실제로 만든 것
- **init**: 객체를 만들 때 자동으로 호출되어 초기 속성을 넣는 메서드
- self: 그 객체 자신. 파이썬이 첫 인자로 자동으로 넘김

### @dataclass

- **init**, **repr**, **eq** 매직 메서드(dunder)를 자동으로 만들어 줌
- 일반 클래스 print → <HoldingPlain object at 0x...>, dataclass → Holding(custodian='Pershing', ...)
- 기본 dataclass는 **hash**가 None이라 unhashable

### == 비교

- 일반 클래스: 같은 객체인지(is) 비교 → 값이 같아도 따로 만들면 False
- dataclass: 선언한 필드 값을 전부 하나씩 비교 → 다 같으면 True, 하나라도 다르면 False
- 같은 클래스여야 함. field(compare=False)로 비교에서 뺄 수 있음
- 용도: 테스트(assert result == expected), 찾기(x in list), 중복 제거(set)

### frozen=True

- 객체를 만든 뒤 필드에 다시 대입하는 걸 막음 (FrozenInstanceError)
- 바꾸려면 dataclasses.replace(h, quantity=200)로 새 객체를 만듦 (문자열 upper()와 같은 방식)
- 값이 안 바뀌니 hashable → dict 키, set 원소 가능 (Day 1: immutable → hashable)
- 얕은 불변: 필드가 list면 그 안쪽은 바뀔 수 있음 (Day 1의 ([1], 2)와 같은 원리)

### 저녁: Holding 리팩터링

- (실습 후 채우기: @property value, @classmethod from_row, 결과가 일요일과 같았는지)

### 저녁: Holding 리팩터링

- custodian_totals.py를 dict(row["..."]) 대신 Holding dataclass로 바꿈, 결과는 일요일과 동일
- @property value: 괄호 없이 h.value로 쓰는 계산 값. quantity × price로 정해지는 값이라 필드로 저장하지 않음 (어긋날 수 없음). 읽기 전용
- @classmethod from_row(cls, row): 객체가 없을 때 클래스에서 바로 불러 객체를 만듦. cls(...) == Holding(...)
- 문자열 → float 변환은 from_row 한 곳에서만
- 타입 힌트(quantity: float)는 자동 변환도 검사도 안 함 → 문자열이 그대로 들어가 TypeError. 검사는 mypy(목요일)
- Holding 한 줄에 대한 일(value, from_row)은 클래스 안, 파일 전체를 다루는 일(custodian_total)은 클래스 밖 함수로
- 클래스 이름은 대문자 시작, 단수(Holding). 들여쓰기가 클래스 소속을 정함

## 2026-11-10 (2주차 화): 예외 처리와 사용자 정의 예외

### 아침: Two Sum II - Input Array Is Sorted

- 출력이 1-indexed → [i + 1, j + 1]. 문제 읽기에서 놓치기 쉬움
- 브루트포스: 이중 for, j는 i + 1부터 (같은 원소 두 번 쓰지 않기) → O(n²), O(1)
- 최적화: 양 끝 투 포인터 → O(n), O(1)
    - total = numbers[left] + numbers[right]
    - total < target → left += 1 (작은 쪽을 키움) / total > target → right -= 1 (큰 쪽을 줄임)
    - left는 오른쪽으로만, right는 왼쪽으로만. 둘 다 가운데로
- left, right 자체가 인덱스, 값은 numbers[left]
- hash 풀이도 가능 (target - num을 dict에서 찾기) → O(n) 시간이지만 O(n) 공간이라 "O(1) extra space" 조건 위반
- 정렬된 입력 + O(1) 공간 요구 = 투 포인터 신호
- 실수: target - left처럼 인덱스로 계산, 이동 방향을 반대로 씀
- 투 포인터 두 종류: 양 끝에서 가운데로(이 문제) vs 같은 방향(슬라이딩 윈도우)

### 복습: Number of Islands

- 범위 밖 = `r < 0 or r >= rows` (부등호를 반대로 써서 모든 칸에서 바로 return)
- `=+ 1`은 +1을 대입, `+= 1`이 더하기 → 에러 없이 결과가 항상 1

### try / except / else / finally

- try: 에러가 날 수 있는 코드만 최소로
- except: try에서 예외가 났을 때
- else: try가 예외 없이 성공했을 때 (if의 else와 다름)
- finally: 성공, 실패, return과 상관없이 항상 마지막 (정리 작업용, with open이 대신 해 줌)

### 넓게 잡으면 위험한 이유

- except:나 except Exception:은 오타(NameError) 같은 버그까지 조용히 숨김
- except:는 Ctrl+C(KeyboardInterrupt)까지 잡음
- 예상하는 예외만 구체적으로 (float 변환 → ValueError)

### raise

- raise 예외(...): 예외를 직접 일으킴
- except 안에서 raise만 쓰면 잡은 예외를 traceback 그대로 다시 던짐 (기록만 하고 넘길 때)

### 사용자 정의 예외와 from e

- class InvalidHoldingError(ValueError): pass → 부모(ValueError)로도 잡힘
- 따로 만드는 이유: 받는 쪽이 "데이터 문제"만 골라 잡고 다른 버그는 드러나게
- except ValueError as e: e는 예외 객체 (메시지, 종류를 꺼낼 수 있음)
- raise NewError(...) from e: 원래 예외를 원인(**cause**)으로 연결 → traceback에 둘 다 남음
  ("The above exception was the direct cause of the following exception")
- f-string의 !r은 따옴표까지 보여 줌 → 빈 문자열 '' 도 눈에 보임

### 실습: 망가진 줄 건너뛰고 보고

- from_row: float 변환 두 줄만 try, 실패하면 InvalidHoldingError from e
- custodian_total: InvalidHoldingError만 잡아서 skipped에 (줄 번호, 이유), continue
- enumerate(reader, start=2): 헤더가 1번 줄이라 실제 파일 줄 번호
- 함수가 (합계, skipped) 두 개를 반환 → result, skipped = custodian_total(p)
- 결과: 망가진 CSV에서도 멈추지 않고 정상 CSV와 같은 합계 + 2줄 보고

### 오늘 걸린 실수

- 경로를 안 바꿔서 정상 CSV를 계속 읽음
- for line_no, row in reader → dict를 둘로 풀려다 "too many values to unpack" → enumerate 필요
- continue 위치: except 안에 있어야 함. try와 같은 높이면 매 줄 건너뜀
- continue가 없으면 이전 줄의 h가 남아 있어서 그 값이 한 번 더 더해짐 (에러 없이 합계가 부풀어서 위험)
- totals 줄이 for 밖으로 나가면 마지막 줄 하나만 더해짐
- 괄호 개수: append((a, str(e)))는 닫는 괄호 3개
- 실무 판단: 금융 데이터는 건너뛰더라도 반드시 보고해야 함 (조용히 틀린 합계가 가장 위험)
