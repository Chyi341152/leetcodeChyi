# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
#
# Example:
#
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
#
#


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dicts = dict(zip(range(len(nums)), nums))
        for i, value in dicts.items():
            complement = target - value
            # Get key by value in dictionary
            if (complement in list(dicts.values())) and list(dicts.keys())[list(dicts.values()).index(complement)] != i:
                return (i, list(dicts.keys())[list(dicts.values()).index(complement)])
        print("No two sum solution")
        return (False,)
