class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def match(lis, tre):
            if not lis:
                return True
            if not tre:
                return False

            if lis.val != tre.val:
                return False

            return match(lis.next, tre.left) or match(lis.next, tre.right)

        def deeper(node):
            if not node:
                return False

            if match(head, node):
                print(node.val)
                return True
            return deeper(node.left) or deeper(node.right)

        return deeper(root)
