a = int(input())
b = int(input())
def evq(a: int, b: int) -> int:

    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
        return a + b

aw = evq(a, b)
print(aw)