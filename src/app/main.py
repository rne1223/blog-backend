from fastapi import FastAPI, APIRouter, Query, HTTPException, Depends

from typing import Optional, Any
from pathlib import Path
from sqlalchemy.orm import Session
from app.schemas.blog import BlogSearchResults, Blog, BlogCreate
from app import deps
from app import crud

# Project Directories
ROOT = Path(__file__).resolve().parent.parent
BASE_PATH = Path(__file__).resolve().parent

app = FastAPI(title="Blog API", openapi_url="/openapi.json")

api_router = APIRouter()

 ## Blog endpoints
@api_router.get("/blog/{blog_id}", status_code=200, response_model=Blog)
def fetch_blog(
    *,
    blog_id: int,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Fetch a single recipe by ID
    """

    result = crud.blog.get(db=db, id=blog_id)
    if not result:
        # the exception is raised, not returned - you will get a validation
        # error otherwise.
        raise HTTPException(
            status_code=404, detail=f"Blog with ID {blog_id} not found"
        )

    return result

@api_router.get("/search/", status_code=200, response_model=BlogSearchResults)
def search_blogs(
    *,
    keyword: Optional[str] = Query(None, min_length=3, example="chicken"),
    max_results: Optional[int] = 10,
    db: Session = Depends(deps.get_db),
) -> dict:
    """
    Search for recipes based on label keyword
    """
    blogs = crud.blog.get_multi(db=db, limit=max_results)
    if not keyword:
        return {"results": blogs}

    results = filter(lambda blog: keyword.lower() in blog.title.lower(), blogs)
    return {"results": list(results)[:max_results]}

@api_router.post("/blog/", status_code=201, response_model=Blog)
def create_recipe(
    *, blog_in: BlogCreate, db: Session = Depends(deps.get_db)
) -> dict:
    """
    Create a new blog in the database.
    """
    blog = crud.blog.create(db=db, obj_in=blog_in)

    return blog 

app.include_router(api_router)


if __name__ == "__main__":
    # Use this for debugging purposes only
    import uvicorn
    uvicorn.run('main:app', host="0.0.0.0", port=8001, log_level="debug", reload=True)
