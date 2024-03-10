from typing import List, Tuple
from collections import Counter
from Readjson import read_json
from measure_performance import measure_performance


@measure_performance
def q3_memory(file_path: str) -> List[Tuple[str, int]]:
    data = read_json(file_path)
    mentioned_counter = Counter()

    for tweet in data:
        if 'mentionedUsers' in tweet:
            mentioned_users = tweet['mentionedUsers']
            if mentioned_users:
                for user in mentioned_users:
                    username = user.get('username')
                    if username:
                        mentioned_counter[username] += 1

    top_10 = mentioned_counter.most_common(10)
    return top_10
