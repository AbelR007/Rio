import typer
from rich.console import Console
from rich.table import Table
from rio_project.core.database import get_db
from rio_project.core.models import Project

app = typer.Typer()
console = Console()

@app.command("create")
def create_project(
    name: str = typer.Option(..., "--name", "-n", help="Name of the project."),
    description: str = typer.Option(None, "--description", "-d", help="Description of the project."),
):
    """
    Creates a new project.
    """
    db_session = next(get_db())
    project = Project(name=name, description=description)
    db_session.add(project)
    db_session.commit()
    db_session.refresh(project)
    console.print(f"Project '{name}' created successfully with ID: {project.id}")

@app.command("list")
def list_projects():
    """
    Lists all projects.
    """
    db_session = next(get_db())
    projects = db_session.query(Project).all()
    
    table = Table(title="Projects")
    table.add_column("ID", style="cyan")
    table.add_column("Name", style="magenta")
    table.add_column("Description", style="green")

    for project in projects:
        table.add_row(str(project.id), project.name, project.description)
    
    console.print(table)
