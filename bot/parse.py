import pytumblr
from random import randint, shuffle

images = []


class Parser:

    def __init__(self):
        self.client = pytumblr.TumblrRestClient('token')

    def parse(self):
        '''
        Many of these are just things needed for debug that'll be deleted after the bot is done.
        '''

        '''
        Trying to avoid repeating images.
        '''

        postnums = [i for i in range(0, 20)]
        shuffle(postnums)
        if len(images) >= 5:
            images.clear()

        img = self.client.tagged('cat', limit=20)[postnums[randint(1, len(postnums)-1)]]['photos'][0]['original_size']['url']

        print(images)  # Debug

        if img not in images:  # If it's not in the latest images list -> Save it, and send to user
            images.append(img)
            return img
        else:
            return self.client.tagged('cat', limit=20)[postnums[randint(1, len(postnums) + 1 )]]['photos'][0]['original_size']['url']


p = Parser()
