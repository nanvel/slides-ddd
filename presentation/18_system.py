""" System - composes the application from the building blocks.

Aka container, composition root, bootstrap script.
"""

class System:
    def __init__(self, settings):
        self.resource = Resource(db_url=settings.db_url)
        self.repository = Repository(self.resource.connection)
        self.use_case = UseCase(self.repository)

        self.resource.init()

    def shutdown(self):
        self.resource.close()


def main():
    system = System(settings)
    try:
        system.use_case()
    finally:
        system.shutdown()
