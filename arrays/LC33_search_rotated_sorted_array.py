class Solution:

    def search(self, nums, target):

        left = 0
        right = len(nums) - 1


        while left <= right:

            mid = (left + right) // 2


            # Target found
            if nums[mid] == target:
                return mid


            # LEFT half sorted
            if nums[left] <= nums[mid]:

                # Target inside LEFT half
                if nums[left] <= target < nums[mid]:
                    right = mid - 1

                # Target not inside LEFT half
                else:
                    left = mid + 1


            # RIGHT half sorted
            else:

                # Target inside RIGHT half
                if nums[mid] < target <= nums[right]:
                    left = mid + 1

                # Target not inside RIGHT half
                else:
                    right = mid - 1


        return -1