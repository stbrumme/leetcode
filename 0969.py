class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        for need in range(len(arr), 0, -1):
            where = arr.index(need)
            # already at correct position
            if where == len(arr):
                continue

            # flip largest value to front
            arr[:where + 1] = arr[:where + 1][::-1]
            yield where + 1

            # flip it to its final position and remove it
            arr = arr[1:need][::-1]
            yield need
