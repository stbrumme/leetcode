class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # compute length
        size = 0
        scan = head
        while scan:
            size += 1
            scan = scan.next

        # find both node
        one  = None
        two  = None
        scan = head
        for i in range(1, size + 1):
            if i == k:
                one = scan
                if two:
                    break
            if i == size - k + 1:
                two = scan
                if one:
                    break

            scan = scan.next

        # swap
        one.val, two.val = two.val, one.val
        return head
