import typer
from rich.console import Console
from rio_project.core.database import get_db, create_db
from rio_project.core.models import Project, Task, Log, Base
import random

app = typer.Typer()
console = Console()

@app.command("seed")
def seed_data():
    """
    Seeds the database with sample data.
    """
    db_session = next(get_db())
    
    # Clear existing data
    db_session.query(Log).delete()
    db_session.query(Task).delete()
    db_session.query(Project).delete()
    
    projects_data = [
        {"name": "Website Redesign", "description": "A complete overhaul of the company website.", "category": "Web"},
        {"name": "Mobile App Development", "description": "Creating a new mobile app for iOS and Android.", "category": "Mobile"},
        {"name": "API Integration", "description": "Integrating a third-party API into our system.", "category": "Backend"},
        {"name": "Marketing Campaign", "description": "A new marketing campaign for the upcoming product launch.", "category": "Marketing"},
        {"name": "Data Analysis Dashboard", "description": "Building a dashboard for data analysis.", "category": "Data"},
        {"name": "Machine Learning Model", "description": "Developing a new ML model.", "category": "Data"},
    ]
    
    projects = []
    for p in projects_data:
        project = Project(name=p['name'], description=p['description'], category=p['category'])
        db_session.add(project)
        projects.append(project)
    
    db_session.commit()

    tasks_data = [
        "Design mockups", "Develop frontend", "Develop backend", "Write documentation",
        "Plan database schema", "Set up CI/CD pipeline", "User testing", "Deploy to production"
    ]

    logs_data = [
        "Initial commit pushed to repository.",
        "Completed the first draft of the design.",
        "Backend API is now functional.",
        "Fixed a critical bug in the authentication flow.",
        "Deployed the latest changes to the staging server."
    ]
    
    for project in projects:
        for _ in range(random.randint(3, 8)):
            task_title = random.choice(tasks_data)
            task = Task(title=task_title, project_id=project.id)
            db_session.add(task)
            db_session.commit() # Commit to get task ID
            for _ in range(random.randint(1, 4)):
                log_content = random.choice(logs_data)
                log = Log(content=log_content, task_id=task.id)
                db_session.add(log)

            
    db_session.commit()
    console.print("[bold green]Database seeded successfully with new data.[/bold green]")

@app.command("clear")
def clear_data():
    """
    Clears all data from the database.
    """
    db_session = next(get_db())
    db_session.query(Log).delete()
    db_session.query(Task).delete()
    db_session.query(Project).delete()
    db_session.commit()
    console.print("[bold yellow]All data has been cleared from the database.[/bold yellow]")
