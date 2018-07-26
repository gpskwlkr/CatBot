import pytumblr
from random import randint, shuffle


class Parser:

    def __init__(self):
        self.client = pytumblr.TumblrRestClient('token')
        self.nums = [i for i in range(0, 20)]
        self.length = len(self.nums)
        self.images = []

    def parse(self):
        '''
        Many of these are just things needed for debug that'll be deleted after the bot is done.
        '''

        '''
        Trying to avoid repeating images.
        '''
        shuffle(self.nums)
        if len(self.images) > 5:
            self.images.clear()

        img = self.client.tagged('cat', limit=20)[self.nums[randint(1, self.length - 1)]]\
            ['photos'][0]['original_size']['url']

        print(self.images)  # Debug

        if img not in self.images:  # If it's not in the latest images list -> Save it, and send to user
            self.images.append(img)
            return img
        else:
            return self.client.tagged('cat', limit=20)[self.nums[randint(1, self.length + 1)]]['photos'][0]['original_size']['url']


p = Parser()
