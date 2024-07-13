class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        data = mountain_arr # just a shorter name

        size = data.length()

        # locate index of maximum value
        def gradient(x):
            return data.get(x) - (0 if x == size - 1 else data.get(x + 1))
        high =       bisect_left(range(size),             0, key = gradient)

        # basic   binary search on left  side
        pos =        bisect_left(range(high),        target, key = lambda x :  data.get(x))
        if pos < high and data.get(pos) == target:
            return pos

        # reverse binary search on right side
        pos = high + bisect_left(range(high, size), -target, key = lambda x : -data.get(x))
        if pos < size and data.get(pos) == target:
            return pos

        return -1
