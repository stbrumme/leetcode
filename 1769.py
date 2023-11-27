class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        left  = 0
        right = sum(int(c) for c in boxes)
        have  = 0
        need  = sum(i if box == "1" else 0 for i, box in enumerate(boxes))

        for i, box in enumerate(boxes):
            yield have + need

            if box == "1":
                left  += 1
                right -= 1
            have += left
            need -= right
