from services import view_task_1, add_task_2, update_task_3, mark_task_4, delete_task_5, search_task_6


def main():
    """Основная функция для запуска программы."""
    while True:
        print("\nМенеджер задач")
        print("1. Просмотр задач")
        print("2. Добавить задачу")
        print("3. Редактировать задачу")
        print("4. Отметить задачу как выполненную")
        print("5. Удалить задачу")
        print("6. Поиск задач")
        print("0. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":  # Просмотр задач
            view_task_1()

        elif choice == "2":  # Добавление задачи
            add_task_2()

        elif choice == "3":  # Редактирование задачи
            update_task_3()

        elif choice == "4":  # Отметка о выполнении
            mark_task_4()

        elif choice == "5":  # Удаление задачи
            delete_task_5()

        elif choice == "6":  # Поиск по слову
            search_task_6()

        elif choice == "0":  # Выход
            break

        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
