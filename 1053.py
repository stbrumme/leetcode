class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        size = len(arr)

        for i in reversed(range(size - 1)):
            # "mismatched" neighbors
            if arr[i] > arr[i + 1]:
                # swap arr[i] with the largest number we can find (not exceeding arr[i] itself)
                high = arr[i + 1]
                pos  = i + 1
                for j in reversed(range(i + 1, size)):
                    if high < arr[j] < arr[i]:
                        high = arr[j]
                        pos  = j

                        if high == arr[i] - 1: # early exit, can't get any closer
                            break

                arr[i], arr[pos] = arr[pos], arr[i]
                break

        return arr
