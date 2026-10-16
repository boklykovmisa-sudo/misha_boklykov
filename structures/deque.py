class Deque:
    def __init__(self):
        self.items = []

    def append_left(self, value):
        self.items.insert(0, value)

    def append_right(self, value):
        self.items.append(value)

    def pop_left(self):
        if not self.items:
            raise IndexError('Deque is empty')
        return self.items.pop(0)

    def pop_right(self):
        if not self.items:
            raise IndexError('Deque is empty')
        return self.items.pop()

    def __len__(self):
        return len(self.items)
