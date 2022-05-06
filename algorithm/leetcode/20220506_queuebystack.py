class MyStack:
    queue1 = []
    queue2 = []

    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self, x: int) -> None:
        self.queue1.append(x)

    def pop(self) -> int:
        x = 0
        while self.queue1:
            self.queue2.append(self.queue1.pop())
            x += 1
        for i in range(x - 1):
            self.queue1.append(self.queue2.pop())
        return self.queue2.pop()

    def top(self) -> int:
        x = 0
        while self.queue1:
            self.queue2.append(self.queue1.pop())
            x += 1
        for i in range(x - 1):
            self.queue1.append(self.queue2.pop())
        answer = self.queue2.pop()
        self.queue1.append(answer)
        return answer

    def empty(self) -> bool:
        return len(self.queue1) == 0


if __name__ == '__main__':
    obj = MyStack()
    print(obj.push(1))
    print(obj.push(2))
    param_2 = obj.pop()
    print(param_2)
    param_3 = obj.top()
    print(param_3)
    param_4 = obj.empty()
    print(param_4)
