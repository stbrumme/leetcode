class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        def digitSum(n):
            result = 0
            while n > 0:
                result += n % 10
                n     //= 10
            return result

        boxes = defaultdict(int)
        for i in range(lowLimit, highLimit + 1):
            boxes[digitSum(i)] += 1
        return max(boxes.values())
