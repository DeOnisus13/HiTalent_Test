class Task:
    """
    Класс для инициализации задач.
    """

    def __init__(self, id: int, title: str, description: str, category: str, due_date: str, priority: str,
                 status: str = "Не выполнена"):
        if not title.strip():
            raise ValueError("Название задачи (title) не может быть пустым")
        self.id = id
        self.title = title.capitalize()
        self.description = description.capitalize()
        self.category = category.capitalize()
        self.due_date = due_date
        self.priority = priority.capitalize()
        self.status = status

    def to_dict(self) -> dict:
        """Метод для представления экземпляра класса Task в виде словаря."""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "category": self.category,
            "due_date": self.due_date,
            "priority": self.priority,
            "status": self.status,
        }

    @staticmethod
    def from_dict(data: dict) -> "Task":
        """Метод для получения экземпляра класса Task из словаря."""
        return Task(**data)

    def __str__(self) -> str:
        """Магический метод для вывода экземпляра класса Task в виде строки."""
        return (f"[{self.id}] {self.title} ({self.category}) - {self.priority}\n"
                f"Выполнить до: {self.due_date}, Статус: {self.status}\n"
                f"{self.description}\n{'-'*50}")
