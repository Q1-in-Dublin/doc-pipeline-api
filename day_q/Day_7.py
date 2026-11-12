# # 1. try / except / else / finally 순서
# def parse(s):
#     try:
#         n = float(s)
#     except ValueError:
#         print("except")
#         return None
#     else:
#         print("else")
#         return n
#     finally:
#         print("finally")

# print(parse("100"))
# print(parse("abc"))

# # 2. 사용자 정의 예외
# class InvalidHoldingError(ValueError):
#     pass

# try:
#     raise InvalidHoldingError("quantity must be a number")
# except ValueError as e:          # 부모로도 잡히는지?
#     print(type(e).__name__, e)

# # 3. from e
# try:
#     try:
#         float("abc")
#     except ValueError as e:
#         raise InvalidHoldingError("bad quantity: 'abc'") from e
# except InvalidHoldingError as e:
#     print(e, "| 원인:", repr(e.__cause__))

def parse(s):
    try:
        return float(s)
    except ValueError:
        print(f"변환 실패: {s!r}")   # 기록만 하고
        raise                        # 같은 예외를 그대로 위로 던짐

parse("abc")