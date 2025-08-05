from typing import List


"""
You are given two arrays of integers, fruits and baskets, each of length n, where fruits[i] represents the quantity of the ith type of fruit, and baskets[j] represents the capacity of the jth basket.

From left to right, place the fruits according to these rules:

Each fruit type must be placed in the leftmost available basket with a capacity greater than or equal to the quantity of that fruit type.
Each basket can hold only one type of fruit.
If a fruit type cannot be placed in any basket, it remains unplaced.
Return the number of fruit types that remain unplaced after all possible allocations are made.
"""
class Solution:
    def numOfUnplacedFruits(self, fruits:List[int], baskets: List[int]) -> int:
        placedBasket = set()    
        
        for i in range(len(fruits)):
            for j in range(len(baskets)):
                if baskets[j] >= fruits[i] and j not in placedBasket:
                    placedBasket.add(j)
                    break
        return len(baskets) - len(placedBasket)
    ##could keep count with an else clause and count, but this solution saves memory. 
    #Any basket that doesn't have a fruit in it means that there is an unplaced fruit
