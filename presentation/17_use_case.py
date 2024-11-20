""" UseCase: service layer pattern -
clearly define where our use cases begin and end.

Entry point into the domain layer.
"""

class CreateUser:
    def __init__(self, users_repository):
        self._users_repository = users_repository

    def __call__(self, email):
        user = User.from_email(email)
        self._users_repository.save(user)


create_user = CreateUser(users_repository)
create_user("john.doe@mail.com")
create_user("jane.doe@mail.com")
