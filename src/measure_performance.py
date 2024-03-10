import psutil
import timeit
from datetime import datetime
from functools import wraps


def measure_performance(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = timeit.default_timer()
        result = func(*args, **kwargs)
        elapsed_time = format(timeit.default_timer() - start_time,".4f")
        execution_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Obtener el uso de memoria del proceso
        process = psutil.Process()
        memory_usage = format(process.memory_info().rss / (1024 * 1024),".4f")  # Convertir a MB

        # Guardar los resultados en un archivo
        with open("performance.txt", "a", encoding="utf-8") as file:
            file.write('**********************************************\n\n')
            file.write(f"Fecha y hora de ejecución: {execution_time}\n")
            file.write(f"Función: {func.__name__}, Tiempo: {elapsed_time} segundos, Uso de memoria: {memory_usage} Mb\n Resultado: {result}\n\n")
        return result
    return wrapper

