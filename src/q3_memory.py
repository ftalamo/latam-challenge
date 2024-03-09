from typing import List, Tuple
from collections import Counter
from Readjson import read_json
from memory_profiler import profile
from datetime import datetime
from format_date import format_date


@profile()
def q3_memory(file_path: str) -> List[Tuple[str, int]]:
    # Inicializar un contador para emojis
    data = read_json(file_path)
    mentioned_counter = Counter()

    # Iterar sobre los tweets y contar menciones
    for tweet in data:
        if 'mentionedUsers' in tweet:
            mentioned_users = tweet['mentionedUsers']
            if mentioned_users:
                for user in mentioned_users:
                    username = user['username']
                    if username:
                        mentioned_counter[username] +=1
    top_10 = mentioned_counter.most_common(10)
    print(top_10)
    pass
