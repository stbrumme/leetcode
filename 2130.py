class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        flat = []
        while head:
            flat.append(head.val)
            head = head.next

        best = float("-inf")
        for i in range(len(flat) // 2):
            best = max(best, flat[i] + flat[-i-1])

        return best
