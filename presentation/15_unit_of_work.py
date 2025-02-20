""" UnitOfWork is an abstraction over the idea of a transaction.
"""

class UniOfWork:
    users_repo: UsersRepo
    events_repo: EventsRepo

    def __init__(self, db):
        self._db = db
        self._session = None

    def __enter__(self):
        self._session = self._db.session().__enter__()
        self.users_repo = UsersRepo(self._session)
        self.events_repo = EventsRepo(self._session)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._session.__exit__(exc_type, exc_val, exc_tb)


uow = UniOfWork(db)
with uow:
    uow.users_repo.save(user)
    uow.events_repo.save(event)
