class Solution:
    def sortSentence(self, s: str) -> str:
        word = s.split()
        word.sort(key=lambda x: int(x[-1]))
        return " ".join(i[:-1] for i in word)
