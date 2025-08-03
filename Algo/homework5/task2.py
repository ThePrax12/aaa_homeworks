import heapq


def merge_k_sorted(arrs: list) -> list:
    ans = []
    iters_arr = [iter(it) for it in arrs]
    min_heap = []
    for idx, it in enumerate(iters_arr):
        value = next(it)
        min_heap.append((value, idx))
    heapq.heapify(min_heap)

    while min_heap:
        value, idx = heapq.heappop(min_heap)
        ans.append(value)
        try:
            value = next(iters_arr[idx])
            heapq.heappush(min_heap, (value, idx))
        except:
            pass
    return ans


def solution():
    arrs = read_multiline_input()  # эта функция уже написана
    merged = merge_k_sorted(arrs)
    print(" ".join([str(el) for el in merged]))


solution()