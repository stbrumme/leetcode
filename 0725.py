class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length = 0
        node = head
        while node:
            length += 1
            node = node.next

        result = []
        while k > 0:
            node = head
            split = (length + k - 1) // k
            for _ in range(split - 1): # process last differently
                if node:
                    node = node.next

            result.append(head)
            if node:
                head = node.next
                node.next = None

            k -= 1
            length -= split

        return result
