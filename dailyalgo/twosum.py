from typing import List
"""Problem info: 
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.


Ex: arr = [3,4,6, 10, 2], target =7     returns [0,1]
"""
arr = [7,0] 
target =7 

arr1 =[5,5]
target = 10


def twoSum(nums: List[int], target: int) -> List[int]:
    res =[]
    for num in nums:
        for num1 in nums:
            if num + num1 == target:
                res.append(nums.index(num))    
                res.append(nums.index(num1))   
                return res


def optimal_two_sum(nums:List[int], target: int) -> List[int]:
    numMap ={} ## hash map
    n = len(nums)
    for i in range(n): ## iterating through array of nums. Hash map stores value: index as key-value pair
        numMap[nums[i]] = i
    print(numMap)

    for i in range(n):
        complement = target -nums[i] # complement = 7-7=0
        if complement in numMap and numMap[complement] !=i: ## if the complement is found in our hash map, and it doesn't have the same index, we can return!
            return [i, numMap[complement]]
        return []
#print(twoSum(arr,target))
print(optimal_two_sum(arr,target))

#numMap[4]= index of 4