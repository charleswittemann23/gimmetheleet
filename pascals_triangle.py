"""
Problem is strong basic building block problem for dynamic programming. 

Pascal's triangle will look like this: 
                1
               1 1
              1 2 1
             1 3 3 1
            1 4 6 4 1
          1 5 10 10 5 1
We will from top of pyramid, and build up until nth row. Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown
Additionally, return answer as array of arrays.
"""
from typing import List
class Solution:
    def generate(self, numRows:int) -> List[List[int]]:
        arr = []
        #Code here!

        return []