import json


def read_json(file_path):
    try:
        tweets = []
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    tweet = json.loads(line)
                    tweets.append(tweet)
                except json.JSONDecodeError as e:
                    print(f"Error al decodificar la línea JSON: {str(e)}")
        return tweets
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {file_path}.")
        return None
