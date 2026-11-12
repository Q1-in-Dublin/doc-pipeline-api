# 1.모듈과 패키지는 뭐가 다른가요? **init**.py는 무슨 역할인가요?

모듈은 models.py가 모듈이다. 패키지는 A folder contain models
**init**.py는 이것이 패키지이다보여주는것 자주쓰는걸 여기꺼내놓으면 from doc_pipeline import holding처럼 짧게 불러쓸수있음

# 2. import x를 하면 실제로 무슨 일이 일어나나요?

import는 x.py에서 파일을 찾고 그파일을 위에서 아래로 한번실행하고, sys.modules라는곳에 케싱함,

# 3. 같은 모듈을 두 번 import하면 파일이 두 번 실행되나요?

처음 한번만 실행된다.

# 4. 지난주에 쓴 if **name** == "**main**":이 오늘부터 왜 꼭 필요해질까요?

실행용코드는 여기에다가 쓴다라는것 정의와 실행란을구분하려고

# 5. 코드를 프로젝트 맨 위가 아니라 src/ 폴더 안에 두는 이유는?

코드를 프로젝트 맨밖에다가 두면 파이썬이 설치된 패키지대신에 지금 폴더의 파일이 실수로 import될수도있다.
?
pyproject.toml, uv.lock, .venv는 각각 뭐고, git에 올리는 건 어느 것인가요?
=> pyproject.toml은프로젝트 설명서(dependency scope), uv.lock은 requemeNts대신쓰는 dependency의 version, venv파이썬 가상환경
