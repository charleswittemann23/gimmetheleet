"""
Given integer array of nums, find the max value possible completing the bitwise OR operation on a subset of nums. TLDR: Look at each possible subset(can delete items in greater array, so order not relevant)
determine if new max val is created after completing bitwise OR, and return the number of times that this max value appears. 
"""
from typing import List
from collections import defaultdict
class Solution: 
    def countMaxOrSubsets(self,nums:List[int]) -> int:
        max_val = 0
        ## this solution relies on the fact that max value is always going to come from "bitwise or"ing every value
        ## this bitwise or operation will only increase the value. Would be different case if xor was used  
        for n in nums:
            max_val |= n
        
        ## not quite dp solution, but relies on at every step, can make the choice to include or exclude value from array. Better word for this would be enumerate? everytime, make a choice to include or exclude, and continue recursion until we reach length of array
        ## best visualization might be tree. Each step, branches down into further decisions
        def enumerate(i, curr_or):
            if i == len(nums):
                return 1 if curr_or == max_val else 0
            include = enumerate(i+1, curr_or | nums[i])
            exclude = enumerate(i+1, curr_or)
            return include + exclude
        
        return enumerate(0,0)
    
    ## alternative solution not hinging on knowing max val
    operations =['&', '|', '^']
    def countMaxgenSubsets(self,nums:List[int], op:str) -> int:
        max_val = 0
        result_map = defaultdict(int) ## hashmap to keep track of all possible values we're finding from enumerated subsets, with value representing their frequency. K: 1 V: 3. The value 1 shows up in three subsets that use _ operation on each element in subset

        n = len(nums)
        def enumerate(i,curr_val):
            if i == n:
                result_map[curr_val] += 1
                max_val = max(max_val, curr_val)
                return
            enumerate(i+1, curr_val)
            ## current general representation not functional, but conveys correct pattern
            enumerate(i+1, curr_val operations[op] nums[i])

        
        enumerate(0,0)
        return result_map[max_val]
    
    def countMaxOrSubsets2(self,nums:List[int]) -> int:
        max_val = 0
        result_map = defaultdict(int) ## hashmap to keep track of all possible values we're finding from enumerated subsets, with value representing their frequency. K: 1 V: 3. The value 1 shows up in three subsets that use _ operation on each element in subset

        n = len(nums)
        def enumerate(i,curr_val):
            if i == n:
                result_map[curr_val] += 1
                max_val = max(max_val, curr_val)
                return
            enumerate(i+1, curr_val)
            ## current general representation not functional, but displays correct pattern
            enumerate(i+1, curr_val | nums[i])

        
        enumerate(0,0)
        return result_map[max_val]

