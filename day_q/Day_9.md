# 1. 타입힌트(x: int, -> str)는 실행할 때 파이썬이 검사하나요? 그럼 왜 쓰나요?

=>들어오는 값이 int인지 return 값이 str인지 알려줌
=> Pydantic이나 fastapi에서는 검사함

# 2. mypy는 언제, 무엇을 검사하나요? 실행과 무슨 차이가 있나요?

타입이맞는지 실제로 검사해준다.

# 3. list[int], dict[str, float], tuple[int, str], str | None은 각각 무슨 뜻인가요?

int 리스트, dictionary인데 키는 str, val은 float , tuple인데 (1,"happy") , str또는 None

# 4.Optional[str]과 str | None은 같은 건가요?

def find(name: str) -> Optional[str]: ... # 옛날 표기 (Python 3.9 이하)
def find(name: str) -> str | None: ...
