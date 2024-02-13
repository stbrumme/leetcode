class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        num = re.sub("0+$", "", num)
        return num if num else "0" # zero is converted to ""
