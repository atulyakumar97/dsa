class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        
        hm = {}
        
        for x in cpdomains:
            y = x.split(' ')
            times = y[0]
            subdomains = y[1].split('.')
            
            j = len(subdomains) - 1
            
            while j >= 0:
                subdomain = '.'.join(subdomains[j:])
                hm[subdomain] = int(times) + hm.get(subdomain, 0)
                j -= 1
                
        ans = []
        
        for key in hm:
            ans.append(str(hm[key]) + ' ' + key)
        
        return ans
            
            