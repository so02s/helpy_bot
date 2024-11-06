import datetime
from typing import Optional, List

from sqlalchemy import select, func, update, case, delete, desc

from db.models import Task, TaskType, PriorityType, Session

# TODO Вообще, если это заработает, можно попробовать шаблонное добавление 
async def add_task(**kwargs):
    """
    Добавляет новую задачу в базу данных.

    Аргументы:
    - title (str): Название задачи (по умолчанию 'Задание без названия').
    - task_type (TaskType): Тип задачи (по умолчанию TaskType.TASK).
    - description (str): Описание задачи (по умолчанию пустая строка).
    - start_datetime (Optional[datetime]): Дата и время начала задачи (по умолчанию None).
    - end_datetime (Optional[datetime]): Дата и время окончания задачи (по умолчанию None).
    - done (bool): Статус выполнения задачи (по умолчанию False).
    - priority (PriorityType): Приоритет задачи.
    """
    
    # Задаем значения по умолчанию
    kwargs.setdefault('title', 'Задание без названия')
    kwargs.setdefault('task_type', TaskType.TASK)
    kwargs.setdefault('description', '')
    kwargs.setdefault('start_datetime', None)
    kwargs.setdefault('end_datetime', None)
    kwargs.setdefault('done', False)
    kwargs.setdefault('priority', PriorityType.LOW)

    # Пытаемся создать объект Task и отфильтровать неподходящие аргументы
    while True:
        try:
            task = Task(**kwargs)  # Пытаемся создать объект Task
            break  # Если успешно, выходим из цикла
        except TypeError as e:
            invalid_arg = str(e).split()[1]
            kwargs.pop(invalid_arg, None)
        except:
            break # Выход при других ошибках

    # Добавление в БД
    async with Session() as session, session.begin():
        try:
            session.add(task)
            session.commit()
        except Exception as e:
            await session.rollback()
            print(f"Ошибка при добавлении задачи: {e}")


async def delete_tasks(tasks_id: List[int]) -> None:
    """
    Удаляет задачи из базы данных по заданному ID.

    Аргументы:
    - task_id (int): ID задач, которые необходимо удалить.
    
    Пропускает задачи, которых нет в БД
    """
    # TODO может не сработать
    async with Session() as session, session.begin():
        await session.execute(
            Task.__table__
            .delete()
            .where(Task.id.in_(tasks_id))
        )


async def update_task(
    task_id: int,
    **kwargs
):  
    """
    Обновляет задачу в базе данных по заданному ID.

    Аргументы:
    - task_id (int): ID задачи, которую нужно обновить.
    - title (str): Новый заголовок задачи.
    - task_type (TaskType): Новый тип задачи (EVENT или TASK).
    - description (str): Новое описание задачи.
    - start_datetime (datetime): Новая дата и время начала задачи.
    - end_datetime (datetime): Новая дата и время окончания задачи.
    - done (bool): Статус выполнения задачи (True или False).
    - priority (PriorityType): Приоритет задачи.
    
    Все неподходящие аргументы пропускаются.

    Исключения:
    - ValueError: Если задача с заданным ID не найдена.
    """
    
    async with Session() as session, session.begin():
        result = await session.execute(
            select(Task)
            .where(Task.id == task_id)
        )
        task = result.scalar_one_or_none()

        if task is None:
            raise ValueError(f"Task with id {task_id} not found")

        for key, value in kwargs.items():
            if value is not None and hasattr(task, key):
                setattr(task, key, value)


async def get_tasks() -> List[Task]:
    """
    Получает все задачи из базы данных.

    Возвращает:
    - List[Task]: Список объектов задач, извлеченных из базы данных.
    """
    async with Session() as session:
        result = await session.execute(
            select(Task)
        )
        return result.scalars().all()