import typer
from rich.console import Console
from rich.table import Table
from rio_project.core.database import get_db
from rio_project.core.models import Task, Project

app = typer.Typer()
console = Console()

@app.command("create")
def create_task(
    title: str = typer.Option(..., "--title", "-t", help="Title of the task."),
    description: str = typer.Option(None, "--description", "-d", help="Description of the task."),
    project_id: int = typer.Option(..., "--project-id", "-p", help="ID of the project this task belongs to."),
):
    """
    Creates a new task.
    """
    db_session = next(get_db())
    project = db_session.query(Project).filter(Project.id == project_id).first()
    if not project:
        console.print(f"Project with ID {project_id} not found.")
        raise typer.Exit(code=1)
    
    task = Task(title=title, description=description, project_id=project_id)
    db_session.add(task)
    db_session.commit()
    db_session.refresh(task)
    console.print(f"Task '{title}' created successfully with ID: {task.id} in project '{project.name}'")

@app.command("list")
def list_tasks(
    project_id: int = typer.Option(..., "--project-id", "-p", help="ID of the project to list tasks for."),
):
    """
    Lists all tasks for a given project.
    """
    db_session = next(get_db())
    project = db_session.query(Project).filter(Project.id == project_id).first()
    if not project:
        console.print(f"Project with ID {project_id} not found.")
        raise typer.Exit(code=1)

    table = Table(title=f"Tasks for Project: {project.name}")
    table.add_column("ID", style="cyan")
    table.add_column("Title", style="magenta")
    table.add_column("Description", style="green")

    for task in project.tasks:
        table.add_row(str(task.id), task.title, task.description)
    
    console.print(table)
