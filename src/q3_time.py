import multiprocessing
from typing import List, Tuple
from collections import Counter
from Readjson import read_json
from measure_performance import measure_performance


@measure_performance
def process_tweet(tweet):
    mentioned_counter = Counter()
    if 'mentionedUsers' in tweet:
        mentioned_users = tweet['mentionedUsers']
        if mentioned_users:
            for user in mentioned_users:
                username = user.get('username')
                if username:
                    mentioned_counter[username] += 1
    return mentioned_counter

def q3_time(file_path: str) -> List[Tuple[str, int]]:
    data = read_json(file_path)
    mentioned_counter = Counter()

    with multiprocessing.Pool() as pool:
        results = pool.map(process_tweet, data)

    for counter in results:
        mentioned_counter.update(counter)

    top_10 = mentioned_counter.most_common(10)
    return top_10
