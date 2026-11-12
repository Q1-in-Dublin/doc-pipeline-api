# d = {}
# d[([1], 2)] = "a"
# => ditionary안에 list랑 int넣는거지
# tuple자체는 immutable이지만 안에 mutable한 list가 들어가면 그 list는 바뀔수있다. tuple의 hash는 원소들의 hash로 만들기때문에
# 하나라도 unhashable이면 tuple도 unhashabled이되서 키로쓸수없다ㅓ

# a = [[1, 2], [3, 4]]
# b = a[:]
# print(a is b)
# print(a[0] is b[0])
#슬라이싱은 shallow copy라서 겉만 복사
#deepcoy는 아예다른값

# s = list(range(n))
# while s:
#     s = s[1:]

# s = [1, 2, 3, 4, 5]
# while s:
#     s = s[1:]
#[[1, 2, 3, 4, 5] 2,3,4,5] 4
#[2, 3, 4, 5] [3,4,5] 3
#[3, 4, 5] [4,5] 2
#[4, 5] [5]1
#copy 10
# n = 5 # 10번
# n = 10 #1000

# i = 0
# while i < len(s):
#     i += 1 

#sharing the list
# def add(item, bucket=[]):
#     bucket.append(item)
#     return bucket

# print(add(1)) #item = 1 bucket = [1]
# print(add(2)) #item = 2 bucket= [1,2]
# print(add(3)) #item = 3 bucket = [1,2,3]

def add(item, bucket = None ):
    if bucket is None :
        bucket = []
    bucket.append(item)
    return bucket
print(add(1)) #item = 1 bucket = [1]
print(add(2)) #item = 2 bucket= [1,2]
print(add(3)) #item = 3 bucket = [1,2,3]

my_list = [1, 2, 3, 4, 5] #를 슬라이싱으로 뒤집기
print(my_list[::-1])

# 7. [[1, 2], [3, 4], [5]]# 를 comprehension 한 줄로 [1, 2, 3, 4, 5]로 만들기
my_list2=[[1, 2], [3, 4], [5]]
print([j for f in my_list2 for j in f])

# 8. range(10)에서 짝수만 제곱한 리스트, 그리고 ["apple", "kiwi", "banana"]로 {"apple": 5, "kiwi": 4, "banana": 6} 만들기
# [i**2 for i in range(10) if i%2 == 0]
[i**2 for i in range(0,10,2)]

#["apple", "kiwi", "banana"]로 {"apple": 5, "kiwi": 4, "banana": 6} 만들기.
from collections import defaultdict,Counter

fruits = ["apple", "kiwi", "banana"]
result = {}
for fruit in fruits:
    result[fruit] = len(fruit)
print(result)