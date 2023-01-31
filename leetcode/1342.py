class Solution:
    def numberOfSteps(self, num: int) -> int:
        step = 0

        while num!=0:
            if num % 2 == 0:
                step += 1
            elif num == 1:
                step += 1
            else:
                step += 2
            num = num //2
        
        return step