TOP_NUMBER = 10
RSS_FEED = 'rss.xml'
SIMILAR = 0.87
import re
from collections import Counter
from difflib import get_close_matches


"""
Shay's output:

* Top 10 tags:
python               10
learning             7
tips                 6
tricks               5
cleancode            5
github               4
pythonic             4
collections          4
beginners            4
virtualenv           4

* Similar tags:
game                 ['games']
challenges           ['challenge']
generator            ['generators']
games                ['game']
challenge            ['challenges']
"""

def get_tags():
    """Find all tags in RSS_FEED.
    Replace dash with whitespace."""
    with open(RSS_FEED, "r") as rf:
        RSS_FEED_CONTENT = rf.read()
    tags_regex = re.compile(r"""<category>([a-z]+)<\/category>""")
    tags_list = re.findall(tags_regex, RSS_FEED_CONTENT)
    return tags_list


def get_top_tags(tags):
    """Get the TOP_NUMBER of most common tags"""
    return Counter(tags).most_common(10)


def get_similarities(tags):
    """Find set of tags pairs with similarity ratio of > SIMILAR"""
    worthy = {}
    for tag in tags:
        temp = get_close_matches(tag, tags, cutoff=SIMILAR)
        if len(temp) > 0:
            for word in temp:
                if word != tag:
                    worthy[tag] = [word]
    return worthy


if __name__ == "__main__":
    tags = get_tags()
    top_tags = get_top_tags(tags)
    print('* Top {} tags:'.format(TOP_NUMBER))
    for tag, count in top_tags:
        print('{:<20} {}'.format(tag, count))
    similar_tags = dict(get_similarities(tags))
    print()
    print('* Similar tags:')
    for singular, plural in similar_tags.items():
        print('{:<20} {}'.format(singular, plural))
