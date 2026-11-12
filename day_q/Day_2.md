1.dict에서 d["x"]와 d.get("x")는 키가 없을 때 각각 어떻게 되나요?
=> None :; d["x"] KeyError : d.get("x")
0.5
2.x in my_list와 x in my_set은 왜 속도가 다른가요? 각각의 복잡도는?
=> 다를거같은데list 는 iterate해서 O(n) Set 은 O(1)
List is comparing one by one / Set is using hash O(1)
1

3.defaultdict(list)는 일반 dict와 무엇이 다르고, 언제 쓰나요?
defaultdict는 key가 없을때 빈배열 반환 dict causes KeyError
0
Counter는 dict와 무엇이 다른가요? most_common()은 뭘 돌려주나요?
Counter is also dictionary keys are element values is the number
Counter has the number 없는키 return 0 not a keyError
most_common() => 전부 많은 순서대로 반환
most_common(2) => 가장 많은거 2개
Counter는 갯수를세는거, dict는 hash기반으로 .. most common은 가장 많이 있는 걸 반환

어제 배운 hashable이 dict 키와 set 원소에 왜 둘 다 필요할까요?
hash 기반은 해쉬함수를 통해서 반환하고 항상 똑같이 변환되기때문에 필요하다. hash값이 저장된뒤 바뀌면 찾아갈수없다.
