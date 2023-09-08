class PeekingIterator:
    def __init__(self, iterator):
        self.i = iterator
        self.cache = None

    def peek(self):
        if self.cache is None:
            self.cache = self.i.next()
        return self.cache

    def next(self):
        if self.cache is None:
            return self.i.next()

        result = self.cache
        self.cache = None
        return result

    def hasNext(self):
        if self.cache is not None:
            return True
        else:
            return self.i.hasNext()
