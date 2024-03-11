from datetime import datetime


def format_date(date):
    try:
        # Convertir la fecha a formato datetime
        fecha_datetime = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S+00:00")

        # Obtener solo la parte de la fecha en formato deseado
        fecha_formateada = fecha_datetime.strftime("%Y,%m,%d")

        return fecha_formateada
    except ValueError:
        raise ValueError("Formato de fecha inválido")

