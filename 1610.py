class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        # camera
        x, y = location
        # points coinciding with the camera
        always = 0

        # compute angle relative to camera
        direction = []
        for px, py in points:
            if px == x and py == y:
                # points always visible when directly at camera's position
                # (unfortunately not clarified in the problem description)
                always += 1
            else:
                dx = px - x
                dy = py - y
                alpha = (180 / pi) * atan2(dy, dx)
                direction.append(alpha)
                direction.append(alpha + 360) # incl. wraparound

        direction.sort()

        result  = 0
        right   = 0
        for left in range(len(direction) // 2):
            low  = direction[left]
            high = angle + low

            while right < len(direction) and direction[right] <= high:
                right += 1

            result = max(result, right - left)

        return result + always
