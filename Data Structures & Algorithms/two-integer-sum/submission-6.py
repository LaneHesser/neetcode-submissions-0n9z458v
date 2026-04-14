class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for i, num in enumerate(nums):
            if num in num_dict and i != num_dict[num]:
                return [num_dict[num], i]

            difference = target - num
            num_dict[difference] = i