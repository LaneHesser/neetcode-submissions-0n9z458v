class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        largest_consecutive, count = 0, 0
        for num in nums:
            if num == 1:
                count += 1
            else:
                largest_consecutive = max(largest_consecutive, count)
                count = 0

        return max(largest_consecutive, count)
