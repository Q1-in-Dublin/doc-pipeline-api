1.def f(x=[])에 계속 append하면 왜 값이 누적되나요?
x라는 빈배열이 있으니까? 2.중첩 리스트에서 b = a, b = a[:], copy.deepcopy(a)는 각각 어떻게 다르게 동작하나요?
=>
b = a #같다
b = a[:] #할당
copy.deepcopy(a) => 값은같지만 a = b 는아니ㅏ
3-1. d = {}일 때 d[(1, 2)] = "a"는 되는데 d[[1, 2]] = "a"는 TypeError: unhashable type: 'list' 에러가 나요. 왜 tuple은 dict 키로 쓸 수 있고 list는 못 쓸까요?
dict 는 hash값으로 값을 찾는다. 그러므로 값이 바뀌면 안된다 그러나 여기에 list를 넣으면 바뀔수있기때문에 어디서 찾을 지 모른다.
mytuple = ("apple", "banana", "cherry")
list = [1,2,3,4]
3-2. 그렇다면 tuple이면 항상 키가 될까요? 안에 list가 들어 있는 tuple ([1], 2)로 d[([1], 2)] = "a"를 하면 어떻게 되고, 그 이유는 뭘까요? 답은 no인가? hashable하지않으면안되는건가?

4.[x for x in range(10**8)]와 (x for x in range(10\*\*8))의 메모리 차이는?
[]는 리스트를만든다. # 수 mb
()는 아무것도만들지않는다. : generator :200 byte 갯수와상관이없음

5.슬라이싱은 새 객체를 만드나요?Yes. Slicing creates a new list, but it’s a shallow copy: the outer list is new, while the elements inside are the same objects.
루프 안에서 s[1:]를 반복하면 복잡도가 어떻게 되나요?

6. [1, 2, 3, 4, 5]를 슬라이싱으로 뒤집기

7. [[1, 2], [3, 4], [5]]를 comprehension 한 줄로 [1, 2, 3, 4, 5]로 만들기
8. range(10)에서 짝수만 제곱한 리스트, 그리고 ["apple", "kiwi", "banana"]로 {"apple": 5, "kiwi": 4, "banana": 6} 만들기
