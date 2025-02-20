"""
Resource - abstraction of application lifetime.
"""
import logging
from contextlib import AbstractContextManager, contextmanager
from typing import Callable

from sqlalchemy import create_engine, orm


class Database:
    def __init__(self, db_uri: str):
        self._engine = create_engine(db_uri)
        self._session_factory = orm.scoped_session(
            orm.sessionmaker(
                autocommit=False,
                autoflush=False,
                bind=self._engine,
            ),
        )

    @contextmanager
    def session(self) -> Callable[..., AbstractContextManager[orm.Session]]:
        session: orm.Session = self._session_factory()
        try:
            yield session
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()

    def shutdown(self):
        self._engine.dispose()


class InitLogging:
    def __init__(self, log_leve="ERROR"):
        self._log_level = log_leve

    def init(self):
        logging.basicConfig(level=self._log_level)
