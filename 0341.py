class NestedIterator:
    def flatten(self, nested):
        if nested.isInteger():
            self.data.append(nested.getInteger())
        else:
            for n in nested.getList():
                self.flatten(n)

    def __init__(self, nestedList: [NestedInteger]):
        self.data = []
        for n in nestedList:
            self.flatten(n)

    def next(self) -> int:
        return self.data.pop(0)

    def hasNext(self) -> bool:
        return len(self.data) > 0
