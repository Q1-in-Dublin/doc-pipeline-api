1. def f(a, b=2, _, c)에서 _ 뒤의 c는 어떻게 넘겨야 하나요? 왜 이런 문법이 있을까요?
   => b는 기본값, \*은 구분선을 본다 뒤에 keyword-only인자로 만드는선
2. def f(*args, \*\*kwargs)에서 함수 안의 args와 kwargs는 각각 무슨 타입인가요? 호출할 때 f(*my_list), f(**my_dict)의 \*, **는 무슨 뜻인가요?
   *args는 이름없이 넘어온 값을 collect해서 반환 tuple로 받음
   *kargs 는 keyboard가 있는 값을 Collect한다 keyword가 있기때문에 dictionary로받는다 3.아래 코드는 왜 UnboundLocalError가 날까요?
   count = 0
   def add():
   count += 1
   add()

    4.방금 푼 Number of Islands에서 dfs 안에서는 grid[r][c] = "0"이 되는데, cnt += 1을 dfs 안에서 하면 에러가 나요. 둘의 차이는? (nonlocal이 힌트)

5.파이썬의 변수 찾는 순서 LEGB는 무엇의 약자인가요?
Local variable
Enclosing function
Global
Built in
