'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.

https://leetcode.com/problems/two-sum/
'''

from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # initialize hash table, (key = num in nums, value = idx in nums)
        lookup_dict = {}
        # O(n)
        for i in range(len(nums)):
            # calculate complement
            lookfor = target - nums[i]
            # check if complement exists in hash table
            if lookfor in lookup_dict:
                return [lookup_dict[lookfor],i]
            # otherwise, we have not found two numbers add up to target
            # store the current nums to hash table
            lookup_dict[nums[i]] = i
    if __name__ == "__main__":
        nums = [-1,0,1,2,-1,-4]
        sol = Solution()
        sol.threeSum(nums)