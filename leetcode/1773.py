class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        c = 0
        if ruleKey == 'type':
            index = 0
        elif ruleKey == 'color':
            index = 1
        elif ruleKey == 'name':
            index = 2
        
        for item in items:
            if item[index] == ruleValue:
                c += 1
        
        return c