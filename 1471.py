class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        # find obscure median
        arr.sort()
        mid = (len(arr) - 1) // 2
        median = arr[mid]

        left  = 0
        right = len(arr) - 1
        for _ in range(k):
            if abs(arr[left] - median) > abs(arr[right] - median):
                yield arr[left]
                left += 1
            else:
                yield arr[right]
                right -= 1
