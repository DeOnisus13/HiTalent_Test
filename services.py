from task_manager import TaskManager
from validators import validate_date

manager = TaskManager()


def view_task_1():
    """Функция для вывода списка задач при выборе в main-функции."""
    category = input("Введите категорию (или оставьте пустым для всех задач): ")
    manager.view_tasks(category if category else None)


def add_task_2():
    """Функция для добавления задачи при выборе в main-функции."""
    while True:
        title = input("Название: ").strip()
        if not title:
            print("Название не может быть пустым")
            continue
        break

    description = input("Описание: ").strip()
    category = input("Категория: ").strip()

    while True:
        due_date = input("Выполнить до (День.Месяц.Год): ").strip()
        try:
            due_date = validate_date(due_date)
            break
        except ValueError as err:
            print(err)

    while True:
        priority = input("Приоритет (низкий, средний, высокий): ").strip().lower()
        if priority not in ["низкий", "средний", "высокий"]:
            print("Некорректный приоритет. Выберите: низкий, средний или высокий")
            continue
        break

    manager.add_task(title, description, category, due_date, priority)


def update_task_3():
    """Функция для редактирования задачи при выборе в main-функции."""
    while True:
        task_id = input("ID задачи: ")
        task_id = int(task_id) if task_id.isdigit() else print(
            "Некорректный ID задачи. Введите другой или 0 для завершения.")
        if task_id == 0:
            break
        elif task_id:
            if not manager.get_task(task_id):
                print(f"Нет задачи с ID {task_id}")
            else:
                print("Введите новые значения (оставьте пустым для пропуска):")
                title = input("Название: ").strip()
                if title == "":
                    title = None  # Не обновляем title, если введен пустой
                description = input("Описание: ").strip()
                category = input("Категория: ").strip()
                due_date = input("Срок (День.Месяц.Год): ").strip()
                if due_date:
                    try:
                        due_date = validate_date(due_date)
                    except ValueError as err:
                        print(err)
                        due_date = None
                priority = input("Приоритет (низкий, средний, высокий): ").strip().lower()
                if priority not in ["низкий", "средний", "высокий", ""]:
                    print("Некорректный приоритет.")
                    priority = None
                manager.update_task(task_id, title=title, description=description, category=category,
                                    due_date=due_date,
                                    priority=priority)
                break


def mark_task_4():
    """Функция для отметки задачи как выполненной при выборе в main-функции."""
    while True:
        task_id = input("ID задачи: ")
        task_id = int(task_id) if task_id.isdigit() else print(
            "Некорректный ID задачи. Введите другой или 0 для завершения.")
        if task_id == 0:
            break
        elif task_id:
            manager.mark_task_done(task_id)
            break


def delete_task_5():
    """Функция для удаления задачи при выборе в main-функции."""
    while True:
        task_id = input("ID задачи: ")
        task_id = int(task_id) if task_id.isdigit() else print(
            "Некорректный ID задачи. Введите другой или 0 для завершения.")
        if task_id == 0:
            break
        elif task_id:
            manager.delete_task(task_id)
            break


def search_task_6():
    """Функция для поиска задачи по словам при выборе в main-функции."""
    keyword = input("Ключевое слово: ")
    manager.search_tasks(keyword)
