# Application structure

DDD doesn't require the use of any specific architecture.
Isolating the domain implementation is a prerequisite for domain-driven design.

A single domain:
```
app/
├─ factories/
│ ├─ product.py
│   ├─ ProductFactory
├─ models/
│ ├─ product.py
│   ├─ Product
├─ repos/
│ ├─ products.py
│   ├─ ProductsRepo
├─ services/
│ ├─ captcha.py
│   ├─ CaptchaService
├─ use_cases/
  ├─ add_product.py
    ├─ AddProduct
```

With subdomains:
```
app/
├─ <core_domain>/
│ ├─ models/
│ ...
├─ <supporting_domain>/
├─ ...
```

Intention-revealing interface - a design in which the names of classes,
methods, and other elements convey both the original developer's purpose 
in creating them and their value to a client developer.

Context is king, especially when implementing DDD.
