from typing import List, Tuple
from collections import Counter
from modules.Readjson import read_json
import re
from modules.measure_performance import measure_performance


@measure_performance
def q2_memory(file_path: str) -> List[Tuple[str, int]]:
    data = read_json(file_path)
    emoji_counter = Counter()

    emoji_pattern = re.compile(
        r'[\U0001F300-\U0001F6FF]|[\U0001F900-\U0001F9FF]|[\U0001F600-\U0001F64F]|[\U0001F680-\U0001F6FF]')

    for tweet in data:
        text = tweet.get('content', '')
        emojis = emoji_pattern.findall(text)
        for emoji in emojis:
            emoji_counter[emoji] += 1

    top_10 = emoji_counter.most_common(10)

    return top_10