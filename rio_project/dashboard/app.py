import random
from flask import Flask, render_template
from rio_project.core.database import get_db
from rio_project.core.models import Project, Task, Log
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from collections import Counter

app = Flask(__name__)

def create_tasks_by_project_chart():
    db_session = next(get_db())
    projects = db_session.query(Project).all()
    project_names = [project.name for project in projects]
    task_counts = [len(project.tasks) for project in projects]

    fig = go.Figure([go.Bar(x=project_names, y=task_counts, marker_color='#007BFF')])
    fig.update_layout(
        title="Tasks per Project",
        xaxis_title="Project",
        yaxis_title="Number of Tasks",
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font_color='white',
        showlegend=False
    )
    return fig.to_html(full_html=False, include_plotlyjs='cdn')

def create_project_category_chart():
    db_session = next(get_db())
    projects = db_session.query(Project).all()
    categories = [project.category for project in projects]
    category_counts = Counter(categories)

    fig = go.Figure([go.Pie(labels=list(category_counts.keys()), values=list(category_counts.values()))])
    fig.update_layout(
        title="Projects by Category",
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font_color='white',
        showlegend=True
    )
    return fig.to_html(full_html=False, include_plotlyjs='cdn')

def create_task_timeline_chart():
    db_session = next(get_db())
    tasks = db_session.query(Task).all()
    
    if not tasks:
        return "No tasks to display in timeline."

    df = pd.DataFrame([
        dict(Task=task.title, Start=task.created_at, Finish=task.created_at + pd.Timedelta(days=random.randint(2,10)), Project=task.project.name) 
        for task in tasks
    ])

    fig = px.timeline(df, x_start="Start", x_end="Finish", y="Task", color="Project")
    fig.update_layout(
        title="Task Timeline",
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font_color='white',
        showlegend=False
    )
    return fig.to_html(full_html=False, include_plotlyjs='cdn')


@app.route("/")
def index():
    db_session = next(get_db())
    projects = db_session.query(Project).all()
    tasks = db_session.query(Task).all()
    logs = db_session.query(Log).order_by(Log.created_at.desc()).limit(10).all()
    
    total_projects = len(projects)
    total_tasks = len(tasks)
    total_logs = db_session.query(Log).count()

    tasks_by_project_chart = create_tasks_by_project_chart()
    project_category_chart = create_project_category_chart()
    task_timeline_chart = create_task_timeline_chart()

    return render_template(
        "index.html",
        total_projects=total_projects,
        total_tasks=total_tasks,
        total_logs=total_logs,
        recent_logs=logs,
        projects=projects,
        tasks=tasks,
        tasks_by_project_chart=tasks_by_project_chart,
        project_category_chart=project_category_chart,
        task_timeline_chart=task_timeline_chart
    )
