# Packages
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

# Modules
from db.postgres_db import Base


class UsersModel(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column()
    last_name: Mapped[str] = mapped_column()
    email: Mapped[str] = mapped_column(unique=True)
    username: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str] = mapped_column()
    role: Mapped[bool] = mapped_column(ForeignKey("roles.name"))
    roles: Mapped["RolesModel"] = relationship(back_populates="users")

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, username={self.username!r}, role={self.role!r})"
