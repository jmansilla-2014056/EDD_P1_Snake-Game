class Stack:
    elements = []

    def __init__(self):
        self.elements = []

    def get_size(self):
        return len(self.elements)

    def push(self, x):
        self.elements.append(x)

    def pop(self):
        if self.size > 0:
            return self.elements.pop()

    def get_peek(self):
        return self.elements[-1]

    peek = property(fget=get_peek)
    size = property(fget=get_size)
