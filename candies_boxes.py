"""super clean solution from Sung Jinwoo"""
"""Basically given boxes, keys, and candies, some up the number of candies you can get by opening all possible boxes"""
class Solution(object):
     def maxCandies(self, status, candies, keys, containedBoxes, initialBoxes):
        foundOpenable = True
        totalCandies =0
        while initialBoxes and foundOpenable:
            foundOpenable = False
            nextBoxes = []
            for boxId in initialBoxes:
                if status[boxId]:
                    foundOpenable = True
                    nextBoxes.extend(containedBoxes[boxId])
                    for keyId in keys[boxId]:
                        status[keyId] = 1
                    totalCandies += candies[boxId]
                else:
                    nextBoxes.append(boxId)
            initialBoxes = nextBoxes

        return totalCandies