import typer
from rich.console import Console
from rio_project.core.database import create_db
from rio_project.cli import project_commands, task_commands, seed_commands, log_commands
from rio_project.dashboard.app import app as flask_app
import webbrowser

app = typer.Typer()
console = Console()

app.add_typer(project_commands.app, name="project")
app.add_typer(task_commands.app, name="task")
app.add_typer(seed_commands.app, name="db")
app.add_typer(log_commands.app, name="log")

@app.command()
def hello(name: str):
    """
    Says hello to the given name.
    """
    console.print(f"Hello [bold green]{name}[/bold green]! Welcome to Rio Project Manager.")

@app.command()
def init_db():
    """
    Initializes the database.
    """
    console.print("Initializing database...")
    create_db()
    console.print("[bold green]Database initialized successfully.[/bold green]")

@app.command()
def dashboard():
    """
    Launches the web-based dashboard.
    """
    console.print("Launching dashboard on http://127.0.0.1:8000")
    webbrowser.open("http://127.0.0.1:8000")
    flask_app.run(port=8000)


if __name__ == "__main__":
    app()
