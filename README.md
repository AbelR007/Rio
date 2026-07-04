
# Rio Project Manager

Rio is a lightweight and powerful project management tool designed for developers who love to work from the command line but also appreciate a visual overview of their work. It combines a rich command-line interface (CLI) with a web-based dashboard to help you manage your projects and tasks efficiently.

## Features

*   **CLI-First:** Manage your projects and tasks directly from your terminal.
*   **Web Dashboard:** A web-based dashboard to visualize your projects and tasks.
*   **Project and Task Management:** Create, list, and manage projects and their associated tasks.
*   **SQLite Backend:** A simple and file-based database for portability.
*   **Interactive Charts:** The dashboard includes interactive charts to visualize your data.

## Tech Stack

*   **Backend:** Python, Flask, SQLAlchemy
*   **CLI:** Typer, Rich
*   **Frontend:** HTML, Plotly, Pandas
*   **Database:** SQLite

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

*   Python 3.7+
*   Git

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/<your-github-username>/Rio.git
    cd Rio
    ```

2.  **Create a virtual environment:**
    ```bash
    python -m venv .venv
    ```

3.  **Activate the virtual environment:**
    *   **Windows:**
        ```bash
        .venv\Scripts\activate
        ```
    *   **macOS/Linux:**
        ```bash
        source .venv/bin/activate
        ```

4.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Initialize the database:**
    ```bash
    python main.py init-db
    ```

## Usage

### Command-Line Interface

The CLI is the primary way to interact with Rio.

*   **Create a project:**
    ```bash
    python main.py project create --name "My First Project" --description "This is my first project."
    ```

*   **List projects:**
    ```bash
    python main.py project list
    ```

*   **Create a task:**
    ```bash
    python main.py task create --title "My First Task" --project-id 1
    ```

*   **List tasks for a project:**
    ```bash
    python main.py task list --project-id 1
    ```

### Web Dashboard

To launch the web dashboard, run the following command:

```bash
python main.py dashboard
```

This will start a local web server, and you can view the dashboard by navigating to `http://127.0.0.1:8000` in your web browser.

## Future Plans

We have many exciting features planned for the future of Rio. Here's a sneak peek at our roadmap:

*   **Task Status and Priority:** Add status (e.g., "To Do", "In Progress", "Done") and priority levels to tasks.
*   **User Authentication:** Add user accounts and authentication to secure your projects.
*   **More Charts and Visualizations:** Enhance the dashboard with more insightful charts and data visualizations.
*   **Task Dependencies:** Allow tasks to have dependencies on other tasks.
*   **Export and Import:** Add functionality to export and import project data.

## Contributing

Contributions are welcome! Please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.
