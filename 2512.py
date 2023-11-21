class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        # faster lookup
        words = {}
        for w in positive_feedback:
            words[w] = +3
        for w in negative_feedback:
            words[w] = -1

        all = []
        for r, id in zip(report, student_id):
            score = sum(words.get(w, 0) for w in r.split(" "))
            all.append(( -score, id )) # highest score first after sorting, therefore negate sign

        all.sort()
        return [ id for score, id in all[:k] ]
