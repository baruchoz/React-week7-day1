# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
# ex.1
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].
# ex. 2
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
#  nums = [2,7,11,15]
# # target = 9
# nums = [3,2,4]
# target = 6

def index_sum(nums, target):
    for i in range(len(nums)):
        for n in range(i + 1, len(nums)):
            if nums[i] + nums[n] == target:
                return [i, n]
            

print(index_sum([2, 7 , 11, 15], 9))        
print(index_sum([3, 2 , 4], 6))        

