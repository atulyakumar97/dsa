class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        
        hm = {}
        c = 0
        
        for val in arr:
            hm[val] = 1 + hm.get(val, 0)
        
        
        for key in hm:
            if key!= 0 and key * 2 in hm:
                return True
            elif key==0 and hm[key] > 1:
                return True
        
        return False