class Solution:
    def interpret(self, command: str) -> str:
        ans = ""
        for i in range(len(command)):
            if command[i] == '(' and command[i+1] == ')':
                ans += 'o'
                continue
            elif command[i] == ')' or command[i] == '(':
                continue
            else:
                ans += command[i]
        return ans
