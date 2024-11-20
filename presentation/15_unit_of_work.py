""" UnitOfWork is an abstraction over the idea of a transaction.
"""

class UniOfWork:
    def __init__(self, connection):
        self._connection = connection
        self.users_repo = UsersRepository(connection)
        self.events_repo = EventsRepository(connection)

    def __enter__(self):
        self._connection.begin()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self._connection.commit()
        else:
            self._connection.rollback()


uow = UniOfWork(connection)
with uow:
    uow.users_repo.save(user)
    uow.events_repo.save(event)
