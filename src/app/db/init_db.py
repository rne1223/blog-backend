import logging
from sqlalchemy.orm import Session

import crud, schemas
from db import base
from recipe_data import RECIPES

logger = logging.getLogger(__name__)

FIRST_SUPERUSER = "admin@recipeapi.com"


# make sure all SQL Alchemy models are import before initializing DB
# otherwise, SQL Alchemy might fail to initialize relations properly
# for more details: https://github.com/tiangolo/full-stack-fastapi-postgresql/issues/28

def init_db(db: Session) -> None:
    # Tables shoudl be created with Alembic migrations
    # But if you don't wnat to use migrations, create
    # the tbales un-commenting the next line
    # Base.metadata.create_all(bind=engine) 
    if FIRST_SUPERUSER:
        user = crud.user.get_by_email(db, email=FIRST_SUPERUSER)
        if not user:
            user_in = schemas.UserCreate(
                full_name="Initial Super User",
                email=FIRST_SUPERUSER,
                is_superuser=True,
            )
            user = crud.user.create(db, obj_in=user_in)
        else:
            logger.warning(
                "Skiping creating superuser. User with email "
                f"{FIRST_SUPERUSER} already exists. "
            )
        
        if not user.recipes:
            for recipe in RECIPES:
                recipe_in = schemas.RecipeCreate(
                    label=recipe["label"],
                    source=recipe["source"],
                    url=recipe["url"],
                    submitter_id=user.id,
                )

                crud.recipe.create(db, obj_in=recipe_in)
    else:
        logger.warning(
            "Skipping creating superuser. FIRST_SUPERUSER needs to be "
            "provided as an env variable. "
            "e.g FIRST_SUPERUSER=admin@api.hello.com"
        )