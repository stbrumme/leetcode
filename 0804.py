class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        result = set()
        for w in words:
            m = ""
            for c in w:
                m += morse[ord(c) - ord("a")]
            result.add(m)
        return len(result)
