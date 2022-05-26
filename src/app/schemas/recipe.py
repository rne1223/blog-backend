from pydantic import BaseModel, HttpUrl

from typing import Sequence


# API Schemas
class RecipeBase(BaseModel):
    lable: str
    source: str
    url: HttpUrl
    
class RecipeCreate(RecipeBase):
    lable: str
    source: str
    url: HttpUrl
    submitter_id: int

class RecipeUpdate(RecipeBase):
    label: str

# DB Schemas
# Properties shared by models stored in DB
class RecipeInDBBase(RecipeBase):
    id: int
    submitter_id: int

    class Config:
        orm_mode = True

class Recipe(RecipeInDBBase):
    pass

# Properties stored in DB
class RecipeInDB(RecipeInDBBase):
    pass

class RecipeSearchResults(BaseModel):
    results: Sequence[Recipe]