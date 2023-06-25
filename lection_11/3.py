class DataObject:
    def __init__(self, data) -> None:
        self.data = data


class Deque:
    def __init__(self) -> None:
        self.deque = []
        self.max_amount = 5
        self.amount = 0

    def append_left(self, data: DataObject):
        if len(self.deque) < 5:
            self.deque = [data] + self.deque
        else:
            print("max len error")

    def append_right(self, data: DataObject):
        if len(self.deque) < 5:
            self.deque = self.deque + [data]
        else:
            print("max len error")

    def pop_left(self):
        self.deque.pop(0)

    def pop_right(self):
        self.deque.pop(len(self.deque) - 1)

data_1 = DataObject({1, 3, "sdf"})
data_2 = DataObject("gh")
data_3 = DataObject(["sdf", 123])

deque = Deque()
deque.append_right(data_1)
deque.append_right(data_2)
deque.append_right(data_3)
deque.append_right(data_2)
deque.append_right(data_1)
print(deque.deque)
deque.append_right(data_3)
print(deque.deque)
deque.pop_right()
deque.append_right(data_3)
print(deque.deque)






