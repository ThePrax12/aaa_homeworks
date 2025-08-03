def is_palindrome(a: int) -> bool:
    digits = []
    n = 0
    while a:
        n += 1
        digits.append(a % 10)
        a = a // 10
    for i in range(n//2 + 1):
        if digits[i] != digits[n - i - 1]:
            return False
    return True


def solution():
    a = int(input())
    c = is_palindrome(a)
    print(c)


solution()