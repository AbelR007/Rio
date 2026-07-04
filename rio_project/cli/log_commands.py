import typer
from rich.console import Console
from rio_project.core.database import get_db
from rio_project.core.models import Task, Log

app = typer.Typer()
console = Console()

@app.command("add")
def add_log(
    task_id: int = typer.Option(..., "--task-id", "-t", help="ID of the task to add the log to."),
    content: str = typer.Option(..., "--content", "-c", help="Content of the log message."),
):
    """
    Adds a new log to a task.
    """
    db_session = next(get_db())
    task = db_session.query(Task).filter(Task.id == task_id).first()
    if not task:
        console.print(f"Task with ID {task_id} not found.")
        raise typer.Exit(code=1)
    
    log = Log(content=content, task_id=task_id)
    db_session.add(log)
    db_session.commit()
    console.print(f"Log added to task {task_id} successfully.")
