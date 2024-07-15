class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums) # speed is what we need

        # convert to an array
        flat = []
        scan = head
        while scan:
            flat.append(scan.val)
            scan = scan.next

        # and back to a list, skip values of nums
        head = None
        for f in reversed(flat):
            if f not in nums:
                head = ListNode(val = f, next = head)

        return head
