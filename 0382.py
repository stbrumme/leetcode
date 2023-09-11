class Solution:
    def __init__(self, head: Optional[ListNode]):
        self.head = head
        self.length = 0
        while head:
            self.length += 1
            head = head.next

    def getRandom(self) -> int:
        pos  = randint(0, self.length - 1)
        node = self.head
        while pos > 0:
            pos -= 1
            node = node.next

        return node.val
