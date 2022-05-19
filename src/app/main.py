from typing import Optional
from fastapi import FastAPI, APIRouter, HTTPException

from schemas import Recipe, RecipeCreate, RecipeSearchResults
from recipe_data import RECIPES


app = FastAPI()
api_router = APIRouter()


@api_router.get("/", status_code=200)
def root() -> dict:
    """
    Root GET
    """
    return {"msg": "Hello World"}

@api_router.get("/recipe/{recipe_id}", status_code=200)
def fetch_recipe(*, recipe_id: int) -> dict:
    """
    Recipe url 
    """

    result = [recipe for recipe in RECIPES if recipe["id"] == recipe_id]
    if not result:
         raise HTTPException(
            status_code=404, detail=f"Recipe with ID {recipe_id} not found"
        )
        
    return result[0] 

@api_router.get("/search/", status_code=200, response_model=RecipeSearchResults)
def search_recipes(
    *,
    keyword: Optional[str] = None,
    max_results: Optional[int] = 10
) -> dict:
    """
    Search url 
    """
    if not keyword:
        return {"results": RECIPES[:max_results]}

    # Search in RECIPES
    results = [recipe for recipe in RECIPES
                if keyword.lower() in recipe["label"].lower()]

    if results:
        return results[:max_results]

@api_router.post("/recipe/", status_code=201, response_model=Recipe)
def create_recipe(*, recipe_in: RecipeCreate) -> Recipe: 
    """"
    Create recipe url 
    """
    new_entry_id = len(RECIPES) + 1
    recipe_entry = Recipe (
        id      = new_entry_id,
        label   = recipe_in.label,
        url     = recipe_in.url,
        source  = recipe_in.source
    )

    RECIPES.append(recipe_entry.dict())

    return recipe_entry 

@api_router.delete("/recipe/{recipe_id}", status_code=200)
def remove_recipe(*, recipe_id: int) -> dict:

    """"
    Deleting a recipe from RECIPE
    """
    result = fetch_recipe(recipe_id=recipe_id)

    if result:
        RECIPES.remove(result)
        return {"detail" : f"REMOVED recipe with ID {recipe_id}"}


    

app.include_router(api_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run('main:app', host="0.0.0.0", port=8080, reload=True, log_level="info")