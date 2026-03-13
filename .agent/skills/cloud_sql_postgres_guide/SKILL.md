---
name: cloud_sql_postgresql_guide
description: DEFINITIVE GUIDE for Cloud SQL for PostgreSQL. MUST be used for any task involving Cloud SQL, PostgreSQL, or database interactions on Google Cloud. Covers MCP tools, google_ml_integration, and safety.
---

# Cloud SQL for PostgreSQL & AI Best Practices

This skill outlines **mandatory rules** for interacting with **Cloud SQL for PostgreSQL** and implementing AI features using `google_ml_integration`.

## 1. Cloud SQL PostgreSQL Interaction

*   **Prioritize MCP Tools**: Always use available MCP tools (e.g., `execute_sql`, `list_tables`, `list_indexes`) over shell commands (e.g., `psql` via `run_command`).
    *   **Bad**: `run_command(CommandLine="psql -c 'SELECT ...'")`
    *   **Good**: `mcp_cloud-sql-postgresql_execute_sql(sql="SELECT ...")`
*   **Schema Discovery**: Do not assume schema. Use tools to check tables and columns first.
    *   `mcp_cloud-sql-postgresql_list_tables()`
    *   `mcp_cloud-sql-postgresql_get_column_cardinality()` creates a good summary.

## 2. AI & Embeddings (`google_ml_integration`)

*   **Use the Extension**: Leverage `google_ml_integration` for in-database embeddings on Cloud SQL.
*   **Model Selection**: Always use `text-embedding-004` unless explicitly instructed otherwise.
*   **Generation Syntax**: Use the `embedding()` function.
    ```sql
    embedding('text-embedding-004', content_column)
    ```
*   **Vector Search & Casting**:
    *   **Crucial**: You MUST cast the embedding result to `vector` for similarity search operators to work.
    *   **Pattern**:
        ```sql
        ORDER BY embedding_column <-> embedding('text-embedding-004', 'query text')::vector LIMIT 5
        ```

## 3. General Rules

*   **Shell Commands**: Avoid `echo $VAR` for DB config if an MCP tool can retrieve it (e.g., `SELECT current_database()`).
*   **Safety**: Always verify `DELETE` or `UPDATE` logic by first running a `SELECT` with the same `WHERE` clause if unsure.
