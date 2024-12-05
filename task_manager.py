import json
from json import JSONDecodeError
from typing import List, Optional

from validators import validate_date
from task import Task


class TaskManager:
    """
    Класс для работы с менеджером задач.
    """

    def __init__(self, file_path: str = "data.json"):
        self.file_path = file_path
        self.tasks: List[Task] = []
        self.load_tasks()

    def load_tasks(self):
        """Метод получения списка задач класса Task из json-файла."""
        try:
            with open(self.file_path, "r", encoding="UTF-8") as f:
                tasks_data = json.load(f)
                self.tasks = [Task.from_dict(task) for task in tasks_data]
        except FileNotFoundError:
            self.tasks = []
        except JSONDecodeError:
            print("Ошибка чтения JSON файла.")

    def save_tasks(self):
        """Метод для сохранения изменений в json-файл."""
        with open(self.file_path, "w", encoding="UTF-8") as f:
            json.dump([task.to_dict() for task in self.tasks], f, ensure_ascii=False, indent=4)

    def add_task(self, title: str, description: str, category: str, due_date: str, priority: str):
        """Метод для добавления новой задачи."""
        if not title.strip():
            raise ValueError("Название задачи (title) не может быть пустым.")

        due_date = validate_date(due_date)

        new_id = max((task.id for task in self.tasks), default=0) + 1
        task = Task(id=new_id, title=title, description=description, category=category, due_date=due_date,
                    priority=priority)
        self.tasks.append(task)
        self.save_tasks()
        print(f"Добавлена новая задача с ID {new_id}")

    def get_task(self, task_id: int) -> Optional[Task]:
        """Метод для получения задачи."""
        return next((task for task in self.tasks if task.id == task_id), None)

    def update_task(self, task_id: int, **kwargs):
        """Метод для редактирования задачи."""
        task = self.get_task(task_id)
        for key, value in kwargs.items():
            if hasattr(task, key) and value:
                setattr(task, key, value)
        self.save_tasks()
        print(f"Задача с ID {task_id} обновлена")

    def mark_task_done(self, task_id: int):
        """Метод для отметки задачи как выполненной."""
        task = self.get_task(task_id)
        if task:
            task.status = "Выполнена"
            self.save_tasks()
            print(f"Задача с ID {task_id} помечена как выполненная")
        else:
            print(f"Нет задачи с ID {task_id}")

    def delete_task(self, task_id: int):
        """Метод для удаления задачи."""
        if not [task for task in self.tasks if task.id == task_id]:
            print(f"Нет задачи с ID {task_id}")
        else:
            self.tasks = [task for task in self.tasks if task.id != task_id]
            self.save_tasks()
            print(f"Задача с ID {task_id} удалена")

    def view_tasks(self, category: Optional[str] = None):
        """Метод для вывода списка задач."""
        filtered_tasks = self.tasks if category is None else [task for task in self.tasks if task.category == category]
        for task in filtered_tasks:
            print(task)

    def search_tasks(self, keyword: str):
        """Метод для поиска задач по ключевым словам."""
        result = [task for task in self.tasks if
                  keyword.lower() in task.title.lower() or keyword.lower() in task.description.lower()]
        for task in result:
            print(task)
