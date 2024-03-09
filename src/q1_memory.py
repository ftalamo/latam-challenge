from typing import List, Tuple
from collections import defaultdict
from datetime import datetime
from Readjson import read_json
from memory_profiler import profile
from datetime import datetime
from format_date import format_date

@profile()
def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    data = read_json(file_path)
    date_counts = defaultdict(int)
    user_counts = defaultdict(lambda: defaultdict(int))
    for tweet in data:
        date = format_date(tweet['date'])
        username = tweet['user']['username']
        date_counts[date] += 1
        user_counts[date][username] += 1

    # Obtener las 10 fechas principales
    top_dates = sorted(date_counts.items(), key=lambda x: x[1], reverse=True)[:10]

    # Obtener el usuario con más publicaciones para cada fecha principal
    result = [(date, max(user_counts[date], key=user_counts[date].get)) for date, _ in top_dates]
    print(result)
    pass

