class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # inject IDs
        id = 0
        current = head
        while current:
            current.id = id
            id += 1
            current = current.next

        all = []
        for _ in range(id):
            all.append(Node(0, None, None))

        # replicate
        id = 0
        current = head
        while current:
            all[id].val = current.val
            if id < len(all) - 1:
                all[id].next = all[id + 1]
            if current.random:
                all[id].random = all[current.random.id]

            current = current.next
            id += 1

        return all[0]
