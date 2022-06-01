from pydantic import BaseModel

from typing import Sequence

# API Schemas
class BlogBase(BaseModel):
    title: str
    body: str
    
class BlogCreate(BlogBase):
    title: str
    body: str
    submitter_id: int

class BlogUpdate(BlogBase):
    body: str

# DB Schemas
# Properties shared by models stored in DB
class BlogInDBBase(BlogBase):
    id: int
    submitter_id: int

    class Config:
        orm_mode = True

class Blog(BlogInDBBase):
    pass

# Properties stored in DB
class BlogInDB(BlogInDBBase):
    pass

class BlogSearchResults(BaseModel):
    results: Sequence[Blog]