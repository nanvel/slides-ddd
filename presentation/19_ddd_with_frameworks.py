"""DDD and Frameworks (Django, Scrapy, FastAPI, etc.)

Django:
- wrap Django ORM within repositories
- call usecases in views, middlewares, manage commands
"""
from aiohttp import web


async def events_handler(request):
    events = await request["system"].get_events()
    return web.json_response({"items": events})


def build_app(system):
    app = web.Application()
    app["system"] = system

    app.on_startup.append(system.init)
    app.on_cleanup.append(system.shutdown)

    app.router.add_get("/api/events", events_handler)

    return app


if __name__ == '__main__':
    system = System()
    app = build_app(system)
    web.run_app(app, host="0.0.0.0", port=8000)


# use dependency injection container + inject decorator + Depends in FastAPI
@router.get("/api/events")
@inject
def get_events(
        limit: int,
        use_case: GetEvents = Depends(Provide[System.get_events]),
    ):
    events = use_case(limit=limit)
    ...
