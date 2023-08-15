class Solution:
    def add(self, root):
        if not root:
            return []

        return [ root.val ] + self.add(root.child) + self.add(root.next)


    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        all = self.add(head)
        size = len(all)

        result = [ Node(all[i], None, None, None) for i in range(size) ]

        for i in range(size):
            if i > 0:
                result[i].prev = result[i-1]
            if i < size - 1:
                result[i].next = result[i+1]

        return result[0]
