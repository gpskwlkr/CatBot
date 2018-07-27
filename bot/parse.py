import pytumblr
from random import randint, shuffle


class Parser:
    
    def __init__(self):
        self.client = pytumblr.TumblrRestClient('token')
        self.nums = [i for i in range(0, 20)]
        self.length = len(self.nums)
        self.images = []
    
    def parse(self, animal):
        """Choosing image & returning URL"""
        
        '''
        Trying to avoid repeating images.
        '''
        shuffle(self.nums)
        randnum = randint(1, self.length)
        print("randnum -%s  "% (randnum))
        img = self.client.tagged(animal, limit=20)[self.nums[randnum]]['photos'][0]['original_size']['url']\
            if randnum < 20 else self.parse(animal)
        
        print(img)
        
        if len(self.images) > 5:
            self.images.clear()
        
        if img not in self.images:  # If it's not in the latest images list -> Save it, and send to user
            self.images.append(img)
            return img
        else:
            self.parse(animal)


p = Parser()

