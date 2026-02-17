# LeetCode 1 - Two Sum
# Link: https://leetcode.com/problems/two-sum/
# Approach: Hashmap to store value -> index
# Time: O(n), Space: O(n)

def twoSum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        need = target - num
        if need in seen:
            return [seen[need], i]
        seen[num] = i