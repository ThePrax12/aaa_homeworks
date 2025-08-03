import heapq


class StreamMedian:
    def __init__(self):
        self.min_heap = []  # min куча с элементами >= медианы
        self.max_heap = []  # max куча с элементами <= медианы
        self.elem_cnt = 0

    def add_num(self, num: int) -> None:
        if self.elem_cnt == 0:
            heapq.heappush(self.min_heap, num)
            self.elem_cnt += 1
            return None

        if self.elem_cnt > 1 and -num >= self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)

        # перераспределяем элементы по кучам, чтобы не было сильного перекоса по количеству
        if len(self.min_heap) < len(self.max_heap):
            popped = heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, -popped)
        elif len(self.min_heap) > len(self.max_heap) + 1:
            popped = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -popped)
        self.elem_cnt += 1

    def find_median(self) -> float:
        if self.elem_cnt == 0:
            return None
        if self.elem_cnt % 2 == 1:
            return self.min_heap[0]

        return (self.min_heap[0] - self.max_heap[0]) / 2


def solution():
    n = int(input())
    stream = StreamMedian()
    for i in range(n):
        line = input().split()
        command = line[0]
        if command == "ADD":
            stream.add_num(int(line[1]))
        elif command == "FIND_MEDIAN":
            print(f"{stream.find_median():.1f}")


solution()