""" Repository methods

- Store an object as data in the persistence layer.
- Find an object based on its relationship to another.
- Reconstitution - creation of an object from stored data.

Repository methods should either modify state or answer questions,
but never both (Command-Query Responsibility Segregation):
- Queries should not have side-effects
- Commands should not return data
"""

class UsersRepository:
    ...


users_repository = UsersRepository()


# bad practice (business logic leaking into a repository)
users_repository.give_a_revard(user_id=1)

# good practice
user = users_repository.get(user_id=1)
user.give_a_revard()
users_repository.save(user)
