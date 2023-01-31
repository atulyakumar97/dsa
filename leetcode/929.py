class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        
        unique_emails = set()
        
        for email in emails:
            
            unique_emails.add(getEmail(email))
        
        return len(unique_emails)

def getEmail(email):
    username, domain = email.split('@')
    cleaned = ""
    
    for char in username:
        if char == '+':
            break
            
        if char.isalnum():
            cleaned += char
        
    return cleaned + '@' + domain