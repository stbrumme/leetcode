class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        # convert discount
        factor = (100 - discount) / 100

        def convert():
            for p in sentence.split(" "):
                # starts with "$", no other "$", only digits
                if p and p[0] == "$" and p[1 :].isnumeric():
                    value = float(p[1 :]) * factor
                    yield f"${value:.2f}" # two decimal places
                else:
                    yield p

        return " ".join(convert())
