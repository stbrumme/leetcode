class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        first = None
        last  = None
        shortest = +inf

        one = head
        two = one.next
        pos = 1 # index of "two"
        while two.next:
            three = two.next

            critical = (one.val < two.val > three.val) or (one.val > two.val < three.val)
            if critical:
                if last is not None:
                    shortest = min(shortest, pos - last)

                if first is None:
                    first = pos

                last = pos

            one  = two
            two  = three
            pos += 1

        return [ -1, -1 ] if shortest == +inf else [ shortest, last - first ]
