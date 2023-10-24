class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        nums = set(nums)

        result = 0
        node   = head
        connected = False
        while node:
            if node.val in nums:
                connected = True
            else:
                if connected:
                    connected = False
                    result   += 1

            node = node.next

        if connected:
            result += 1
        return result
