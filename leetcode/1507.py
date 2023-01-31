class Solution:
    def reformatDate(self, date: str) -> str:
        
        [d, m, y]= date.split(' ')
        
        months = {"Jan": "01",
                  "Feb": "02",
                  "Mar": "03",
                  "Apr": "04",
                  "May": "05",
                  "Jun": "06", 
                  "Jul": "07",
                  "Aug": "08",
                  "Sep": "09",
                  "Oct": "10",
                  "Nov": "11",
                  "Dec": "12"}
        
        return y + '-' + months[m] + '-' + self.correction(d[:-2])
    
    def correction(self, s):
        if int(s) <= 9:
            return '0' + s
        else:
            return s
        