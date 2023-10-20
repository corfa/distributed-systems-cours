from aiohttp import web

from api.v1 import get_tasks
from context import AppContext

def wrapper_handler(handler,context):
    async def wrapper(request):
        return await handler(request,context)
    return wrapper

def setup_routes(app: web.Application, ctx: AppContext):
    app.router.add_get(
        '/v1/get/tasks',
        wrapper_handler(
        get_tasks.handle,
        ctx,
        )
    )