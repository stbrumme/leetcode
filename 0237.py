class Solution:
    def deleteNode(self, node):
        prev = node
        while node.next:
            node.val = node.next.val
            prev = node
            node = node.next

        prev.next = None
