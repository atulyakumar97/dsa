class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        final = []
        length = len(nums)
        for i in range(0, 2*length):
            if i < length:
                final.append(nums[i])
            else:
                final.append(nums[i-length])
        return final
        