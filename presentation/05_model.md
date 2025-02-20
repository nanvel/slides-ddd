# Model

Entity Object: a domain object whose attributes may change 
but that has a recognizable identity over time.

Value object: an immutable domain object whose attributes entirely define it.
It is fungible with other identical objects.

Aggregate: a cluster of associated objects that we treat as a unit 
for the purpose of data changes. Defines and enforces a consistency boundary.

Data Transfer Object: is a data structure designed to hold an entire number of attributes
that need to be transferred to another layer.

Event: represents something that happened.

Command: represents a job that the system should perform.

---

Relying exclusively on the language's standard library's 
primitive data types - such as strings, integers, 
or dictionaries - to represent concepts of the business domain 
is known as the primitive obsession code smell.
