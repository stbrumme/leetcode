class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        yield celsius + 273.15
        yield celsius * 9/5 + 32
