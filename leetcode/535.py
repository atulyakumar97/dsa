import random
import string

class Codec:
    
    hm = {}
    tinyUrlPrefix = 'http://tinyurl.com/'

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        shortUrl = self.tinyUrlPrefix + ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        self.hm[shortUrl] = longUrl
        
        return shortUrl
        
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        
        return self.hm[shortUrl]
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))