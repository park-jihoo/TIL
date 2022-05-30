import heapq


class SeatManager:

    def __init__(self, n: int):
        self.unreserved = list(range(1, n + 1))

    def reserve(self) -> int:
        return heapq.heappop(self.unreserved)

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.unreserved, seatNumber)


if __name__ == '__main__':
    obj = SeatManager(5)
    print(obj.reserve())
    print(obj.reserve())
    print(obj.unreserve(2))
    print(obj.reserve())
    print(obj.reserve())
    print(obj.reserve())
    print(obj.reserve())
    print(obj.unreserve(5))

# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)