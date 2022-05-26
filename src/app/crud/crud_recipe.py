from crud.base import CRUDBase
from models.recipe import Recipe
from schemas.recipe import RecipeCreate, RecipeUpdate

class CRUDrecipe(CRUDBase[Recipe, RecipeCreate, RecipeUpdate]):
    pass

recipe = CRUDrecipe(Recipe)