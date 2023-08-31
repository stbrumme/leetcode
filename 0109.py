class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        # flatten
        all = []
        while head:
            all.append(head.val)
            head = head.next

        # divide'n'conquer
        def deeper(left, right):
            if left > right:
                return None

            pivot = (left + right) // 2
            return TreeNode(all[pivot], deeper(left, pivot - 1), deeper(pivot + 1, right))

        return deeper(0, len(all) - 1)
