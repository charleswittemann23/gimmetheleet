"""
an array of integers, target: int

return the indices of the integers 
exactly 1 solution

return 
Input: nums = [2,7,11,15], target = 9
Output: [0,1]

"""


def two_sum(nums:list, target:int) -> list:
    mymap = {}

    for index, num in enumerate(nums):
        mymap[num] = index
    #print(mymap)
    for index,num in enumerate(nums):
        complement = target - num
        if complement in mymap:
            if mymap[complement]!= index:
                return [index, mymap[complement]]


nums = [2,7,11,15]
target = 9
print(two_sum(nums,target))
test1 = [3,2,4] 
target1 = 6
print(two_sum(test1, target1))
test2 = [3,3] 
target2 = 6
print(two_sum(test2, target2))