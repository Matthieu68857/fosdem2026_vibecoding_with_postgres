# Antigravity & Cloud SQL for PostgreSQL MCP Demo

This project demonstrates how Antigravity and the built-in Model Context Protocol (MCP) server for Cloud SQL for PostgreSQL work together to seamlessly introduce AI features into an existing application.

## Demo Recording

[Watch the Demo on YouTube](https://www.youtube.com/watch?v=SIYaprGTWts&feature=youtu.be)

## Prerequisites

- **Python 3.x**
- **Google Cloud Project** with the Cloud SQL Admin API enabled.
- **Cloud SQL for PostgreSQL Instance**.
- **Antigravity** installed and configured.

## Setup Instructions

### 1. Database Creation

To run this demo, you need a Cloud SQL for PostgreSQL instance with a database configured.

1.  Connect to your Google Cloud Console.
2.  Create a **Cloud SQL for PostgreSQL** instance.
3.  Ensure the `cloudsql.enable_google_ml_integration` database flag is set to `on`.
4.  Create a database named `flowers` inside that instance.
5.  Configure the Antigravity integration to connect to this database via the built-in MCP server. The integration handles the connection and provides the agent with the necessary context and SQL execution capabilities.
6.  Connect to the `flowers` database and run the `setup.sql` script to create the `products` table and insert sample data. You can do this via `psql` or any database client:
    ```bash
    psql -h <your_db_host> -U <your_db_user> -d flowers -f setup.sql
    ```

### 2. Python Virtual Environment

Always run the app inside an isolated Python virtual environment:

```bash
# 1. Create the virtual environment
python3 -m venv .venv

# 2. Activate the virtual environment
source .venv/bin/activate

# 3. Install the dependencies
pip install -r requirements.txt
```

### 3. Running the App

The application uses FastAPI and Uvicorn. To spin up the dev server with hot-reloading:

```bash
source .venv/bin/activate
source .env
uvicorn app:app --reload
```

## Running the Demo

To start the demo, you execute the instructions contained in `prompt.md` by passing it to the agent:

1. Trigger Antigravity with the `prompt.md` file.
2. The agent will use the built-in MCP tools for Cloud SQL PostgreSQL to analyze the existing schema (in the `flowers` database) and determine which extensions are installed.
3. The agent will then create and request approval for an **Implementation Plan**.
4. The execution of the plan will showcase how semantic search (using `google_ml_integration` and `vector` operators) is applied to the current app through both code updates (`app.py` / HTML templates) and live database updates performed through MCP.

## Resetting the Demo

Once the demo is finished and you want to start over:

1. Clean the database by dropping any newly-created AI vector columns, indexes, and extensions (e.g., `vector`, `google_ml_integration`) from the `flowers` database.
2. Revert all local file modifications by running:

```bash
git reset --hard && git clean -fd
```
