class Solution:
    def countPoints(self, rings: str) -> int:
        
        hm = {}
        c = 0
        rgb = {'R': True, 'G': True, 'B': True}.keys()
        
        for i in range(0, len(rings), 2):
            if rings[i+1] in hm:
                hm[rings[i+1]].update({rings[i]: True})
            else:
                hm[rings[i+1]] = {rings[i]: True}
        
        for key, val in hm.items():
            if val.keys() == rgb:
                c += 1
        
        return c

# hm = { 
#     0: {'R': True, 'G': True, 'B': True},
#     1: {'R': True, 'G': True, 'B': True}
# }
