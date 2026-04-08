class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pCount = Counter(p)
        sCount = defaultdict(int)
        l = 0
        res = []

        for r in range(len(s)):
            sCount[s[r]] += 1
            if r - l + 1 > len(p):
                sCount[s[l]] -= 1
                if not sCount[s[l]]:
                    sCount.pop(s[l])
                l += 1
            if pCount == sCount:
                res.append(l)
        return res