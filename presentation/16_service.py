""" Service - a stateless object that implements the business logic.

> Sometimes, it just isn't a thing.
>
> Eric Evans, Domain-Driven Design

Piece of logic that belongs in the domain model
but doesn't sit naturally inside a stateful entity or value object.

A good service characteristics:
- Not a natural part of an entity or value object
- The interface is defined in terms of other elements of the domain model
- The operation is stateless

Use for:
- Significant business process
- Transform domain object from one composition to another
- Calculate a value from multiple domain objects
- Interact with external services
"""

class MailService:
    def __init__(self, host, username, password):
        ...

    def send(self, mail):
        pass

    def receive(self):
        pass
