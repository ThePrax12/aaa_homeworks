def max_even_sum(numbers: list) -> int:
    odds = [i for i in numbers if i % 2 == 1]
    if len(odds) % 2 == 0:
        return sum(numbers)
    return sum(numbers) - min(odds)


def solution():
    numbers = [int(x) for x in input().split()]
    result = max_even_sum(numbers)
    print(result)


solution()
