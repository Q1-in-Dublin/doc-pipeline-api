1.try, except, else, finally는 각각 언제 실행되나요?
=> try :특정걸 실행했을때(에러날수있는부분)
=> except try문에서 예외
else: 성공했을때
finally 코드가 다실행되고나서 꼭 실행되는부분
2.except:나 except Exception:으로 전부 잡으면 왜 위험한가요?
hide bugs
3.raise는 뭘 하고, except 안에서 raise만 쓰면 어떻게 되나요?
특정 오류를 일으킴, raise는 여기서 해결할수는없지만 기록남길때

4.내 예외 클래스를 만들려면 어떻게 하고, 왜 ValueError를 그대로 쓰지 않고 따로 만들까요?
raise NewError(...) from e의 from e는 뭘 남겨 주나요?
class InvalidHoldingError(ValueError):
pass
