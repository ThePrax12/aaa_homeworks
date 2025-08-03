def two_minimals(min1: int, min2: int, num: int) -> tuple:
    if num <= min1:
        min1, min2 = num, min1
    elif num < min2:
        min2 = num
    return min1, min2


def max_div3_sum(numbers: list) -> int:
    min_mod1, min2_mod1, min_mod2, min2_mod2 = max(numbers) + 1, max(numbers) + 1, max(numbers) + 1, max(numbers) + 1
    ans, mod1_cnt, mod2_cnt = 0, 0, 0
    for num in numbers:
        ans += num
        if num % 3 == 1:
            mod1_cnt += 1
            min_mod1, min2_mod1 = two_minimals(min_mod1, min2_mod1, num)
        elif num % 3 == 2:
            mod2_cnt += 1
            min_mod2, min2_mod2 = two_minimals(min_mod2, min2_mod2, num)

    if ans % 3 == 1:
        if mod1_cnt == 0:
            return ans - min_mod2 - min2_mod2
        return ans - min(min_mod1, min_mod2 + min2_mod2)
    if ans % 3 == 2:
        if mod2_cnt == 0:
            return ans - min_mod1 - min2_mod1
        return ans - min(min_mod2, min_mod1 + min2_mod1)
    return ans


def solution():
    numbers = [int(x) for x in input().split()]
    result = max_div3_sum(numbers)
    print(result)


solution()
