class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        end = len(nums)
        newLen = end - nums.count(val)   
        count = newLen
        r = end-1
        i = 0
        while count > 0 and i < end-1:
            while nums[i] == val and r >= 0:
                # swap with right pointer
                tmp = nums[i]
                nums[i] = nums[r]
                nums[r] = tmp
                r -= 1
            i += 1
            count -= 1
        return newLen
