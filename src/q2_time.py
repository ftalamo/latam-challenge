from typing import List, Tuple
from collections import Counter
from modules.Readjson import read_json
from modules.measure_performance import measure_performance
import re
import multiprocessing
from functools import partial


def process_tweet(tweet, emoji_pattern):
    text = tweet.get('content', '')
    emojis = emoji_pattern.findall(text)
    return emojis

@measure_performance
def q2_time(file_path: str) -> List[Tuple[str, int]]:
    data = read_json(file_path)
    emoji_counter = Counter()

    emoji_pattern = re.compile(
        r'[\U0001F300-\U0001F6FF]|[\U0001F900-\U0001F9FF]|[\U0001F600-\U0001F64F]|[\U0001F680-\U0001F6FF]')

    with multiprocessing.Pool() as pool:
        process_tweet_partial = partial(process_tweet, emoji_pattern=emoji_pattern)
        results = pool.map(process_tweet_partial, data)

    for emojis in results:
        for emoji in emojis:
            emoji_counter[emoji] += 1

    top_10 = emoji_counter.most_common(10)

    return top_10