class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int("0b"+a, 2) + int("0b"+b,2))[2:]


class Solution2:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a) - 1
        j = len(b) - 1
        c = ""
        carry = 0

        while i >= 0 or j >= 0:
            sum = 0

            if i >= 0:
                sum += int(a[i])

            if j >= 0:
                sum += int(b[j])

            sum += carry

            if sum == 0:
                digit = 0
                carry = 0
            elif sum == 1:
                digit = 1
                carry = 0
            elif sum == 2:
                digit = 0
                carry = 1
            else:
                digit = 1
                carry = 1

            c = str(digit) + c

            i -= 1
            j -= 1

        if carry == 1:
            c = str(carry) + c

        return c
