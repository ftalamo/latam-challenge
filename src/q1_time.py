from typing import List, Tuple
from datetime import datetime
import multiprocessing
from modules.measure_performance import measure_performance
from modules.format_date import format_date
from modules.Readjson import read_json

def process_tweets(data_chunk):
    date_counts = {}
    user_counts = {}
    for tweet in data_chunk:
        try:
            date = format_date(tweet['date'])
            username = tweet['user']['username']
            date_counts[date] = date_counts.get(date, 0) + 1
            user_counts[date] = user_counts.get(date, {})
            user_counts[date][username] = user_counts[date].get(username, 0) + 1
        except KeyError as e:
            print(f"Error: Clave faltante en tweet: {e}")
    return date_counts, user_counts

@measure_performance
def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
    data = read_json(file_path)
    chunk_size = 3000  # Tamaño del chunk
    results = []

    try:
        with multiprocessing.Pool() as pool:
            chunks = [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]
            processed_chunks = pool.map(process_tweets, chunks)

        # Combinar resultados de todos los chunks
        date_counts = {}
        user_counts = {}
        for date_count, user_count in processed_chunks:
            for date, count in date_count.items():
                date_counts[date] = date_counts.get(date, 0) + count
            for date, users in user_count.items():
                user_counts[date] = user_counts.get(date, {})
                for user, count in users.items():
                    user_counts[date][user] = user_counts[date].get(user, 0) + count

        # Obtener las 10 fechas principales
        top_dates = sorted(date_counts.items(), key=lambda x: x[1], reverse=True)[:10]

        # Obtener el usuario con más publicaciones para cada fecha principal
        results = [(date, max(user_counts[date], key=user_counts[date].get)) for date, _ in top_dates]

    except Exception as e:
        print(f"Error: {e}")

    return results
