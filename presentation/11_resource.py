"""
Resource - abstraction for application lifetime.
"""
import logging

from sqlalchemy import create_engine


class InitPg:
    def __init__(self, db_uri, pool_size=5):
        self._db_uri = db_uri
        self._pool_size = pool_size
        self._engine = None

    def init(self):
        self._engine = create_engine(self._db_uri, pool_size=self._pool_size)

    def shutdown(self):
        self._engine.dispose()

    @property
    def connection(self):
        return self._engine.connect()


class InitLogging:
    def __init__(self, log_leve="ERROR"):
        self._log_level = log_leve

    def init(self):
        logging.basicConfig(level=self._log_level)
