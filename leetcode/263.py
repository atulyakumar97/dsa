class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 0:
            return False

        while n % 2 == 0 or n % 3 == 0 or n % 5 == 0:
            if n%2 == 0:
                n = n / 2
            elif n % 3 == 0:
                n = n / 3
            elif n % 5 == 0:
                n = n / 5

        if n == 1:
            return True
        else:
            return False


class Solution2:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        if n % 2 == 0:
            while n % 2 == 0:
                n /= 2
        if n % 3 == 0:
            while n % 3 == 0:
                n /= 3
        if n % 5 == 0:
            while n % 5 == 0:
                n /= 5
        return n == 1
