class Solution:
    def capitalizeTitle(self, title: str) -> str:
        title = title.split(' ')
        
        for i in range(len(title)):
            if len(title[i]) <= 2:
                title[i] = title[i].lower()
            else:
                title[i] = title[i][:1].upper() + title[i][1:].lower()
        
        return ' '.join(title)
