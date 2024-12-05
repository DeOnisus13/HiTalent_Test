import pytest
import tempfile
import os
from task_manager import TaskManager


@pytest.fixture
def temp_task_manager():
    """Фикстура для создания временного TaskManager для тестов."""
    with tempfile.NamedTemporaryFile(delete=False, suffix=".json") as tmp_file:
        temp_file_path = tmp_file.name
    manager = TaskManager(file_path=temp_file_path)
    yield manager
    os.remove(temp_file_path)


def test_add_task(temp_task_manager):
    """Тест для проверки добавления задачи."""
    manager = temp_task_manager
    manager.add_task(
        title="Тест добавления",
        description="Описание теста добавления",
        category="Тест",
        due_date="25.12.2024",
        priority="Средний"
    )
    assert len(manager.tasks) == 1
    assert manager.tasks[0].title == "Тест добавления"
    assert manager.tasks[0].due_date == "25.12.2024"


def test_view_tasks(temp_task_manager):
    """Тест для проверки просмотра задач."""
    manager = temp_task_manager
    manager.add_task(
        title="Тест просмотра 1",
        description="Описание 1",
        category="Категория 1",
        due_date="01.01.2024",
        priority="Высокий"
    )
    manager.add_task(
        title="Тест просмотра 2",
        description="Описание 2",
        category="Категория 2",
        due_date="02.02.2024",
        priority="Средний"
    )
    assert len(manager.tasks) == 2
    # Проверяем фильтрацию по категории
    filtered_tasks = [task for task in manager.tasks if task.category == "Категория 1"]
    assert len(filtered_tasks) == 1
    assert filtered_tasks[0].title == "Тест просмотра 1"


def test_search_tasks(temp_task_manager):
    """Тест для проверки поиска задач."""
    manager = temp_task_manager
    manager.add_task(
        title="Тест по поиску",
        description="Поиск по описанию",
        category="Поиск",
        due_date="03.03.2024",
        priority="Низкий"
    )
    manager.add_task(
        title="Задача тест",
        description="Описание тестовой задачи",
        category="Тест",
        due_date="04.04.2024",
        priority="Средний"
    )
    # Поиск по названию
    search_results = [task for task in manager.tasks if "поиску" in task.title]
    assert len(search_results) == 1
    assert search_results[0].description == "Поиск по описанию"
    # Поиск по описанию
    search_results = [task for task in manager.tasks if "задачи" in task.description]
    assert len(search_results) == 1
    assert search_results[0].title == "Задача тест"


def test_delete_task(temp_task_manager):
    """Тест для проверки удаления задачи."""
    manager = temp_task_manager
    manager.add_task(
        title="Тест удаления",
        description="Тест для удаления",
        category="Удалить",
        due_date="05.05.2024",
        priority="Высокий"
    )
    assert len(manager.tasks) == 1
    task_id = manager.tasks[0].id
    manager.delete_task(task_id)
    assert len(manager.tasks) == 0


def test_update_task(temp_task_manager):
    """Тест для проверки обновления задачи."""
    manager = temp_task_manager
    manager.add_task(
        title="Тест редактирования",
        description="Тест для редактирования",
        category="Редактировать",
        due_date="06.06.2024",
        priority="Низкий"
    )
    task_id = manager.tasks[0].id
    manager.update_task(
        task_id,
        title="Отредактированный тест",
        description="Отредактированное описание",
        category="Отредактированная категория",
        due_date="07.07.2024",
        priority="Высокий"
    )
    updated_task = manager.tasks[0]
    assert updated_task.title == "Отредактированный тест"
    assert updated_task.description == "Отредактированное описание"
    assert updated_task.category == "Отредактированная категория"
    assert updated_task.due_date == "07.07.2024"
    assert updated_task.priority == "Высокий"
