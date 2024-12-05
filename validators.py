from datetime import datetime


def validate_date(input_date: str) -> str:
    """Проверяет и форматирует дату в формате day.month.year."""
    try:
        date_obj = datetime.strptime(input_date, "%d.%m.%Y")
        return date_obj.strftime("%d.%m.%Y")  # Возвращаем форматированную строку
    except ValueError:
        raise ValueError("Некорректный формат даты. Ожидается dd.mm.yyyy.")
