# Packages
from sqlalchemy.orm import Mapped, mapped_column

# Modules
from db.postgres_db import Base


class BooksModel(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column()
    abbreviation: Mapped[str] = mapped_column()
    language: Mapped[str] = mapped_column()
    cover_image: Mapped[str] = mapped_column()
    normal_price: Mapped[int] = mapped_column()
    marathon_price: Mapped[int] = mapped_column()
    size: Mapped[int] = mapped_column()

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, title={self.title!r}, language={self.language!r})"
