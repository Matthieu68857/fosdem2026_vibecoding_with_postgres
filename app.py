
import os
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import sqlalchemy

db_user = os.environ.get("CLOUD_SQL_POSTGRES_USER")
db_pass = os.environ.get("CLOUD_SQL_POSTGRES_PASSWORD")
db_name = os.environ.get("CLOUD_SQL_POSTGRES_DATABASE")
db_host = os.environ.get("DB_HOST")

db_pool = sqlalchemy.create_engine(
    sqlalchemy.engine.url.URL.create(
        drivername="postgresql+pg8000",
        username=db_user,
        password=db_pass,
        database=db_name,
        host=db_host,
    ),
)

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "results": []})

@app.get("/api/search")
async def api_search(request: Request, q: str):
    query = sqlalchemy.text("SELECT * FROM products WHERE to_tsvector('english', description) @@ plainto_tsquery('english', :query) LIMIT 9")
    with db_pool.connect() as conn:
        rows = conn.execute(query, {"query": q}).mappings().all()

    results = []
    for r in rows:
        result = dict(r)
        result['picture'] = f"/static/images/flowers/{result['product_id']}.png"
        # Truncate description here as well for consistency
        result['description'] = result['description'][:100] + '...' if len(result['description']) > 100 else result['description']
        results.append(result)
        
    return results
