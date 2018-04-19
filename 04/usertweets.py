from collections import namedtuple
import csv
import os

import tweepy

from config import CONSUMER_KEY, CONSUMER_SECRET
from config import ACCESS_TOKEN, ACCESS_SECRET

DEST_DIR = 'data'
EXT = 'csv'
NUM_TWEETS = 100


def auth():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    api = tweepy.API(auth)
    return api


class UserTweets(object):
    """#todo TODOs:
    - create a tweepy api interface
    - get all tweets for passed in handle
    - optionally get up until 'max_id' tweet id
    - save tweets to csv file in data/ subdirectory
    - implement len() an getitem() magic (dunder) methods"""

    def __init__(self, HANDLE, max_id=None, api=auth()):
        self.HANDLE = HANDLE
        self.max_id = max_id
        self.api = api
        self.tweet_template = namedtuple('tweet', ['text', 'id_str', 'created_at'])
        self._tweets = [self.tweet_template(k._json['text'], k._json['id_str'], k._json['created_at']) for k in
                        self.api.user_timeline(self.HANDLE, count=100, max_id=None, page=1)]
        self.to_csv()

    def to_csv(self):
        csv_writer = csv.writer(open(os.path.join(DEST_DIR, f"Twitter_{self.HANDLE}." + f"{EXT}"), "w"))
        csv_writer.writerow(['id_str', 'created_at', 'text'])
        csv_writer.writerows([(twee.id_str, twee.created_at, twee.text) for twee in self._tweets])
        # return self._tweets

    def __len__(self):
        return len(self._tweets)

    def __getitem__(self, position):
        return self._tweets[position]


if __name__ == "__main__":

    for handle in ('pybites', 'elonmusk', 'bbelderbos'):
        print('--- {} ---'.format(handle))
        user = UserTweets(handle)
        for tw in user[:5]:
            print(tw)
