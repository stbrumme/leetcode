class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        seen = set()

        scan = headA
        while scan:
            seen.add(scan)
            scan = scan.next

        scan = headB
        while scan:
            if scan in seen:
                return scan
            scan = scan.next

        return None
