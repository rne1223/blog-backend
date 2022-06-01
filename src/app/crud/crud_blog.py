from app.crud.base import CRUDBase
from app.models.blog import Blog 
from app.schemas.blog import BlogCreate, BlogUpdate

class CRUDblog(CRUDBase[Blog, BlogCreate, BlogUpdate]):
    pass

blog = CRUDblog(Blog)