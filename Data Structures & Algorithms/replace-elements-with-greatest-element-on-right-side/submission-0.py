class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        i, j = 0, len(arr) - 1
        largest = arr[j]
        while j > -1:
            current_largest = largest
            largest = max(arr[j], largest)
            arr[j] = current_largest
            j -= 1

        arr[-1] = -1
        return arr