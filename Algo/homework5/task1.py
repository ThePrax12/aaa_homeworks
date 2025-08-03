import heapq


def get_kth_element(arr: list, k: int):
    heapq.heapify(arr)
    for _ in range(k):
        heapq.heappop(arr)
    return arr[0]


def solution():
    arr = list(map(int, input().split()))
    k = int(input())
    print(get_kth_element(arr, k))


solution()