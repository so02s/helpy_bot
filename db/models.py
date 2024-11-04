import datetime
import enum

from decouple import config
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship, DeclarativeBase, mapped_column, Mapped
from sqlalchemy.ext.asyncio import AsyncAttrs, create_async_engine, async_sessionmaker
from typing import Optional, List

DATABASE_URL = f"postgresql+asyncpg://{config('DB_USER')}:{config('DB_PASS')}@{config('DB_HOST')}/{config('DB_NAME')}"

engine = create_async_engine(url=DATABASE_URL, echo=True)
Session = async_sessionmaker(engine, expire_on_commit=False)

async def create_all_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


class Base(AsyncAttrs, DeclarativeBase):
    pass

# --------------- Для заданий

class TaskType(enum.Enum):
    EVENT = "event"
    TASK = "task"

class PriorityType(enum.Enum):
    HIGH = "high"
    MIDDLE = "middle"
    LOW = "low"

class Task(Base):
    __tablename__ = 'tasks'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    task_type: Mapped[TaskType] = mapped_column(Enum(TaskType), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(String(500), nullable=True)
    start_datetime: Mapped[datetime] = mapped_column(DateTime(), nullable=True, default=None)
    end_datetime: Mapped[datetime] = mapped_column(DateTime(), nullable=True, default=None)
    done: Mapped[bool]
    priority: Mapped[PriorityType] = mapped_column(Enum(PriorityType), nullable=False)
    
    
    # TODO Переделать связи - плак
    # # ID предыдущей задачи
    # previous_task_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey('tasks.id'), nullable=True)
    
    # # Связь с предыдущей задачей
    # previous_task: Optional['Task'] = relationship("Task", remote_side=[id], backref="next_tasks")

    # # Связь с следующими задачами
    # next_tasks: List['Task'] = relationship("Task", back_populates="previous_task")
    


