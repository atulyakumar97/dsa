from collections import defaultdict
from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        s_dict = collections.Counter(s[0:len(p)])
        p_dict = collections.Counter(p)
        
        ans = []
        
        for i in range(0, len(s)-len(p)+1):
               
            
            if i != 0:
                if s_dict[s[i-1]] == 1:
                    del s_dict[s[i-1]]
                else:
                    s_dict[s[i-1]] -= 1
                
                if s[i+len(p)-1] in s_dict:
                    s_dict[s[i+len(p)-1]] += 1
                else:
                    s_dict[s[i+len(p)-1]] = 1
                
            
            if s_dict == p_dict:
                ans.append(i)
        
        return ans
             
##Runtime: 3664 ms - original solution
##Runtime: 420 ms - optimized solution
