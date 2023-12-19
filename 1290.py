class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        result = 0
        while head:
            result *= 2
            result += head.val
            head    = head.next
        return result
