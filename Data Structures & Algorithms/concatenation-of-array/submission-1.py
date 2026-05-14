class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        j = 0
        length = len(nums) * 2
        new_array = [0] * length

        for i in range(len(new_array)):
            new_array[i] = nums[j]
            j += 1

            if j == len(nums):
                j = 0

        return new_array