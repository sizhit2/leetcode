'''
Given an array of integers numbers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

Return the indices of the two numbers (1-indexed) as an integer array answer of size 2, where 1 <= answer[0] < answer[1] <= numbers.length.

You may assume that each input would have exactly one solution and you may not use the same element twice.

 

Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
 

Constraints:

2 <= numbers.length <= 3 * 104
-1000 <= numbers[i] <= 1000
numbers is sorted in increasing order.
-1000 <= target <= 1000
Only one valid answer exists.

https://leetcode.com/problems/two-sum-ii-input-array-is-sorted
'''

from typing import List
class Solution:
    # left right 版本
    def twoSum1(self, numbers: List[int], target: int) -> List[int]:
        lookup = {}
        left,right = 0, len(numbers)-1
        # we do not want to consider the case when left == right 
        while left < right:
            sum = numbers[left] + numbers[right]
            # if sum is too big, we gonna move right pointer to left
            if sum > target:
                right -= 1
                # keep moving until we found a different numbers 
                while numbers[right] == numbers[right + 1] and left < right:
                    right -= 1
            # if sum is too small, we gonna we left pointer to right
            elif sum < target: 
                left += 1
                while numbers[left] == numbers[left - 1] and left < right:
                    left += 1
            # sum == target 
            else:
                # add 1 to consider 1-indexed 
                return [left + 1,right + 1]
            
    # hash table 版本 
    def twoSum2(self, numbers: List[int], target: int) -> List[int]:
        lookup = {}
        for i in range(len(numbers)):
            lookfor = target - numbers[i]
            if lookfor in lookup:
                return [lookup[lookfor] + 1, i+1]
            lookup[numbers[i]] = i
            
            
        