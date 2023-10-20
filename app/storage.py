import typing as tp

from context import AppContext
import models

async def get_tasks(context: AppContext) -> tp.List[models.Task]:
    sql = '''
    select * from tasks
          '''
    rows = await context.db.fetch(sql)

    return [
        models.Task.from_db(row) for row in rows
    ]