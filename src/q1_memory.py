from typing import  List, Tuple
from collections import defaultdict
from datetime import datetime
from Readjson import read_json
from format_date import format_date
from measure_performance import measure_performance


@measure_performance
def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    data = read_json(file_path)
    date_user_counts = defaultdict(lambda: defaultdict(int))

    for tweet in data:
        date = format_date(tweet['date'])
        username = tweet['user']['username']
        date_user_counts[date][username] += 1

    # Obtener las 10 fechas principales
    top_dates = sorted(date_user_counts.keys(), key=lambda date: sum(date_user_counts[date].values()), reverse=True)[:10]

    # Obtener el usuario con más publicaciones para cada fecha principal
    result = [(date, max(date_user_counts[date], key=date_user_counts[date].get)) for date in top_dates]

    return result
