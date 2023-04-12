# Packages
from enum import Enum
from pydantic import BaseModel


class Language(Enum):
    english = "english"
    marathi = "marathi"
    hindi = "hindi"


class Size(Enum):
    normal = "normal"
    pocket = "pocket"
    small = "small"


class BooksAddSchema(BaseModel):
    title: str
    abbreviation: str
    language: Language
    cover_image: str
    normal_price: int
    marathon_price: int
    quantity: int
    size: Size


class BooksUpdateSchema(BaseModel):
    title: str
    abbreviation: str
    language: Language
    cover_image: str
    normal_price: int
    marathon_price: int
    quantity: int
