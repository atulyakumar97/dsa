from typing import List


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        num2 = []

        while k > 0:
            num2 = [k % 10] + num2
            k = k // 10

        i = len(num) - 1
        j = len(num2) - 1
        carry = 0
        sum = []

        while i >= 0 or j >= 0:
            digit = 0

            if i >= 0:
                digit += num[i]

            if j >= 0:
                digit += num2[j]

            digit += carry

            if digit >= 10:
                carry = digit // 10
                digit = digit % 10
            else:
                carry = 0
                digit = digit % 10

            i -= 1
            j -= 1

            sum = [digit] + sum

        if carry:
            sum = [carry] + sum

        return sum


class Solution2:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:

        i = len(num) - 1
        carry = 0
        sum = []

        while i >= 0 or k > 0:
            digit = 0

            if i >= 0:
                digit += num[i]

            if k > 0:
                digit += k % 10

            digit += carry

            carry = digit // 10
            digit = digit % 10

            i -= 1
            k = k // 10

            sum.append(digit)

        if carry:
            sum.append(carry)

        return sum[::-1]
