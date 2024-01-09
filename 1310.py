class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        # similar to a prefix sum, but XOR instead of +
        zorro = [ 0 ] # zorro[i] = arr[0] ^ arr[1] ^ ... ^ arr[i - 1]
        for a in arr:
            zorro.append(a ^ zorro[-1])

        return [ zorro[left] ^ zorro[right + 1] for left, right in queries ]
