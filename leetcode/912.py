from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        n = len(nums)

        if n <= 1:
            return nums

        m_p = n // 2

        l_list, r_list = Solution().sortArray(nums[:m_p]), Solution().sortArray(nums[m_p:])
        l_p = r_p = 0

        result = []

        while l_p < m_p or r_p < n - m_p:
            if l_p == m_p:
                result.append(r_list[r_p])
                r_p += 1
            elif r_p == n - m_p:
                result.append(l_list[l_p])
                l_p += 1
            elif l_list[l_p] < r_list[r_p]:
                result.append(l_list[l_p])
                l_p += 1
            else:
                result.append(r_list[r_p])
                r_p += 1

        return result
