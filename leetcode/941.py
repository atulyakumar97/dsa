class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
        if len(arr) < 3:
            return False
        
        peak = max(arr)
        
        if arr[0] == peak or arr[-1] == peak:
            return False
        
        peak_reached = False
        
        for i in range(len(arr)-1):
            if arr[i] == peak:
                peak_reached = True
            
            if peak_reached:
                if arr[i] <= arr[i+1]:
                    return False
            else:
                if arr[i] >= arr[i+1]:
                    return False
                
        return True
                
            