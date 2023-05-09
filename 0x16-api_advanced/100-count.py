#!/usr/bin/python3
""" raddit api"""

import json
import requests


def count_words(subreddit, word_list, after="", count=[]):
    """count all words"""

    if after == "":
        count = [0] * len(word_list)

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(url,
                           params={'after': after},
                           allow_redirects=False,
                           headers={'user-agent': 'bhalut'})

    if response.status_code == 200:
        data = response.json()

        for topic in (data['data']['children']):
            for word in topic['data']['title'].split():
                for k in range(len(word_list)):
                    if word_list[k].lower() == word.lower():
                        count[k] += 1

        after = data['data']['after']
        if after is None:
            save = []
            for k in range(len(word_list)):
                for l in range(k + 1, len(word_list)):
                    if word_list[k].lower() == word_list[l].lower():
                        save.append(l)
                        count[k] += count[l]

            for k in range(len(word_list)):
                for l in range(k, len(word_list)):
                    if (count[l] > count[k] or
                            (word_list[k] > word_list[l] and
                             count[l] == count[k])):
                        aux = count[k]
                        count[k] = count[l]
                        count[l] = aux
                        aux = word_list[k]
                        word_list[k] = word_list[l]
                        word_list[l] = aux

            for k in range(len(word_list)):
                if (count[k] > 0) and k not in save:
                    print("{}: {}".format(word_list[k].lower(), count[k]))
        else:
            count_words(subreddit, word_list, after, count)
