class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        s_dict = dict.fromkeys(sentence)
        return len(s_dict) == 26