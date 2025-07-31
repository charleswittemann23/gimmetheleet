import heapq
class Solution:
    def clearStars(self, s: str) -> str:
        heap = [] ## min heap I believe
        deleted = set() ## set of deleted indices

        for i, char in enumerate(s):
            if char =='*': ## if character we find is a star
                char,neg = heapq.heappop(heap) ##pop smallest lex char
                deleted.add(-neg) ##add it's index to deleted set
            else: 
                heapq.heappush(heap, (char,-i)) ##otherwise we can add char to min-heap

        res = []
        for i,c in enumerate(s):
            if i in deleted or c =='*': continue ##don't do anything if star or deleted char
            res.append(c)
        return ''.join(res)