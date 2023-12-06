class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        # scan forward to the "red zone"
        one = list1
        for _ in range(a - 1):
            one = one.next

        # find end of "red zone"
        two = one
        for _ in range(b + 1 - (a - 1)):
            two = two.next

        # add list2 to first half of list1
        one.next = list2
        while one.next:
            one = one.next
        # add second half of list1
        one.next = two

        return list1
