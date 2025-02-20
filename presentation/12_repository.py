""" Repository pattern - an abstraction over the idea of persistent storage.

Prevent non-domain concepts (database structure) from leaking into your model.

Pros:
- a simple interface between persistent storage and the domain model
- communicate design decisions about object access
- easy to make a fake version of the repository, or swap different storage solutions
- creating domain model before thinking about persistence
- complete control over how we map our objects to tables

Cons:
- ORM already allows swapping to another database solution
- mapping maintenance requires extra work
- adds a "WTF factor" for programmers who are not familiar with repository pattern

Repositories work with aggregates.
"""
from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Optional

import sqlalchemy as sa
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column, sessionmaker


class EventTable(DeclarativeBase):
    __tablename__ = "events"

    id: Mapped[int]

    type: Mapped[int]
    text: Mapped[str]

    created_at: Mapped[datetime] = mapped_column(
        default=datetime.utcnow,
        index=True
    )
    updated_at: Mapped[datetime] = mapped_column(
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
    )

    __table_args__ = (sa.PrimaryKeyConstraint("id"),)


class EventType(int, Enum):
    INQUERY = 1
    SALE = 2


@dataclass(frozen=True)
class Event:
    id: Optional[int]
    type: EventType
    text: str


class EventsRepository:
    def __init__(self, session: Session):
        self._session = session

    def save(self, event: Event) -> int:
        if event.id is None:
            record = EventTable(
                type=event.type.value,
                text=event.text,
            )
        else:
            record = self._session.query(EventTable).get(event.id)
            record.type = event.type.value
            record.text = event.text

        self._session.add(record)

        if record.id is None:
            self._session.flush()
            self._session.refresh(record)

        return record.id

    def get(self, event_id: int) -> Event:
        record = self._session.query(EventTable).get(event_id)

        return Event(
            id=record.id,
            type=EventType(record.type),
            text=record.text,
        )
