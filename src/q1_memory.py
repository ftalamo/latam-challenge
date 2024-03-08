from typing import List, Tuple
from datetime import datetime
from Readjson import Readjson

def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    file = Readjson(file_path)
    data = file.read()
    print(data)
    pass