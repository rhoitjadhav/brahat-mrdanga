# Packages
from sqlalchemy.orm import Mapped, mapped_column, relationship

# Modules
from db.postgres_db import Base


class RolesModel(Base):
    __tablename__ = "roles"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    users: Mapped["UsersModel"] = relationship(back_populates="roles")
