# Summary

| Model                 |     Factory     |       Resource       |  Repository  |            Service            |   UseCase   |   System    |
|-----------------------|:---------------:|:--------------------:|:------------:|:-----------------------------:|:-----------:|:-----------:|
| Data + business logic | Object creation | Application lifetime | Data storage | Business logic outside models |  Interface  |  Composer   |
| Event                 |  EventFactory   |      PgResource      |  EventsRepo  |          MailService          |  GetEvents  |   System    |
| global                |    injected     |       injected       |   injected   |           injected            |  injected   |   global    |
| stateful              |    stateless    |      stateless       |  stateless   |           stateless           |  stateless  |  stateless  |

Domain-driven design pays off best for ambitious projects, 
and it does require strong skills. Not all projects are ambitious.
