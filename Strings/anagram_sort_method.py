class Solution:
    def anagram(self, s:str, t: str) ->bool:
        return sorted(s)== sorted(t)