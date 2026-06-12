class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # remove all occurrences of val in place
        # return number of elements in nums that aren't equal to val
        # 

        count, start, end = 0, 0, len(nums) - 1
        while start < end:
            if nums[start] == val:
                nums[start], nums[end] = nums[end], nums[start]
                end -= 1
            else:
                start += 1

        for i in range(0, end + 1):
            if nums[i] != val:
                count += 1
        
        return count