class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []
        for [i, w1] in enumerate(words):
            for [j, w2] in enumerate(words):
                if i != j and w1 in w2:
                    res.append(w1)
                    break
        return res