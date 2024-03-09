from typing import List, Tuple
from collections import Counter
from Readjson import read_json
from memory_profiler import profile
from datetime import datetime
from format_date import format_date
import re

@profile()
def q2_memory(file_path: str) -> List[Tuple[str, int]]:
    # Inicializar un contador para emojis
    data = read_json(file_path)
    emoji_counter = Counter()

    # Patrón de expresión regular para encontrar emojis
    emoji_pattern = re.compile(
        r'[\U0001F300-\U0001F6FF]|[\U0001F900-\U0001F9FF]|[\U0001F600-\U0001F64F]|[\U0001F680-\U0001F6FF]')

    # Iterar sobre los tweets y contar emojis
    for tweet in data:
        text = tweet.get('content', '')  # Obtener el texto del tweet
        emojis = emoji_pattern.findall(text)  # Encontrar emojis en el texto
        emoji_counter.update(emojis)  # Actualizar contador de emojis

    # Obtener los 10 emojis más utilizados
    top_10 = emoji_counter.most_common(10)

    print(top_10)
    pass