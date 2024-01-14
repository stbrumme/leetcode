class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # flatten the list
        flat = []
        scan = head
        while scan:
            flat.append(scan.val)
            scan = scan.next

        # partial reversal
        result = []
        group  = 1
        while flat:
            # last group might be shorter
            group = min(group, len(flat))
            if group & 1: # odd
                result += flat[:group]
            else:         # even => reverse
                result += flat[:group][::-1]
            del flat[:group]

            group += 1

        # convert back to a list
        pos  = 0
        scan = head
        while scan:
            scan.val = result[pos]
            scan = scan.next
            pos += 1

        return head
