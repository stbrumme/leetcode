class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        result = []

        pos  = 0
        seen = []
        while head:
            heappush(seen, ( head.val, len(result) ))
            result.append(0) #  no bigger node known so far

            while seen:
                # check current node against min-heap
                value, where = seen[0]
                if value >= head.val:
                    break

                # update previous nodes that carry a smaller value
                result[where] = head.val
                heappop(seen)

            head = head.next

        return result
