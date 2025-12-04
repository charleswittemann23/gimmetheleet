class Solution(object):
    def minimizeMax(self, nums, p):
        """
        :type nums: List[int]
        :type p: int
        :rtype: int
        """
        if p == 0:
            return 0
        nums.sort() ## need to sort for binary search of difference. Don't have to check every possible pair, only adjacent pairs in sorted list
        n = len(nums) ## number of items in list

        left, right = 0, nums[-1] - nums[0] ##looking at all possible differences we are going to search for. Can't have negative because it is absolute diff, greatest diff is biggest number - smallest number

        while left < right:
            mid = left + (right - left) //2
            pairs = 0
            i = 1

            while i < n :
                if nums[i] - nums[i-1] <= mid:
                    pairs+=1
                    i+=1
                i+=1
                if pairs >= p:
                    right = mid
                else:
                    left = mid + 1
        return left