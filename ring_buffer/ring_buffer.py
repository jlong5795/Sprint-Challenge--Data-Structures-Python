class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = []

    def append(self, item):
        self.buffer.append(item)
        if len(self.buffer) == self.capacity:
            self.cur = 0
            self.__class__ = self.__Full

    def get(self):
        return self.buffer

    class __Full:
        def __init__(self, n):
            raise

        def append(self, x):
            self.buffer[self.cur] = x
            self.cur = (self.cur + 1) % self.capacity

        def get(self):
            return self.buffer
