import typer
from rich.console import Console

app = typer.Typer()
console = Console()

@app.command()
def hello(name: str):
    """
    Says hello to the given name.
    """
    console.print(f"Hello [bold green]{name}[/bold green]! Welcome to Rio Project Manager.")

@app.command()
def dashboard():
    """
    Launches the web-based dashboard.
    """
    console.print("Launching dashboard...")
    # This will be implemented later
    console.print("[yellow]Dashboard functionality is not yet implemented.[/yellow]")


if __name__ == "__main__":
    app()
