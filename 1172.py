class DinnerPlates:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stacks   = [ [] ]
        self.partial  = [ 0 ] # index of not-yet-full stacks

    def push(self, val: int) -> None:
        if not self.partial:
            # add a new stack (empty)
            self.partial = [ len(self.stacks) ]
            self.stacks.append([])

        # store value
        index = min(self.partial)
        self.stacks[index].append(val)

        # stack is full ?
        if len(self.stacks[index]) == self.capacity:
            self.partial.remove(index)

    def pop(self) -> int:
        # remove empty stacks from the end
        while len(self.stacks) > 1 and not self.stacks[-1]:
            self.partial.remove(len(self.stacks) - 1)
            self.stacks.pop()
        # and invoke our generic function
        return self.popAtStack(-1)

    def popAtStack(self, index: int) -> int:
        if index == -1:
            index = len(self.stacks) - 1

        # invalid request ?
        if index >= len(self.stacks):
            return -1
        if len(self.stacks[index]) == 0:
            return -1

        # that stack was full, now it isn't anymore
        if len(self.stacks[index]) == self.capacity:
            self.partial.append(index)

        return self.stacks[index].pop()
