
class Solution:
    seen = set()
    def containsDuplicate(self, nums):
        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        return False