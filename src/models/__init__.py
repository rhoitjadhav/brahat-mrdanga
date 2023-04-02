# Packages
from .books import BooksModel
from .users import UsersModel

from db.postgres_db import Base, engine

Base.metadata.create_all(engine)
