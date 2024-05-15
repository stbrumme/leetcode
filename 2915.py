class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        todo = { 0: 0 }

        for n in nums:
            # sequences without n
            next = todo.copy()

            # sequences with n
            for total, length in todo.items():
                if total + n <= target: # must not exceed target
                    length += 1
                    total  += n
                    # take care of other longer sequences with the same sum
                    if total not in next or next[total] < length:
                        next[total] = length

            todo = next

        return todo[target] if target in todo else -1
