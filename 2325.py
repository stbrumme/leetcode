class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        mapping = { " ": " " }
        next    = "a"
        for k in key:
            if k not in mapping:
                mapping[k] = next
                next = chr(ord(next) + 1)

        return "".join(mapping[c] for c in message)
