from collections import OrderedDict

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        hm = OrderedDict()
        
        for i in range(len(arr)):
            hm[arr[i]] = 1 + hm.get(arr[i], 0)
        
        c = 0
        for key_pair in hm.items():
            if key_pair[1] == 1:
                c += 1
                if k == c:
                    return key_pair[0]
        return ""