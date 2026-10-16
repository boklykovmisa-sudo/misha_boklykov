class DynamicArray:
    def __init__(self):
        self.items = []

    def append(self, value):
        self.items.append(value)

    def get(self, index):
        return self.items[index]

    def remove_at(self, index):
        return self.items.pop(index)

    def __len__(self):
        return len(self.items)
