from typing import List
from typing import Optional
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy import Table
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

class Base(DeclarativeBase):
    pass

fandom_story_assoc = Table(
    "fandom_story_assoc",
    Base.metadata,
    Column("fandom_id", ForeignKey("fandom.id")),
    Column("story_id", ForeignKey("story.id")),
)

class Category(Base):
    __tablename__ = "category"
    id: Mapped[int] = mapped_column(primary_key=True)
    label: Mapped[str] = mapped_column(String(255))
    fandoms: Mapped[List["Fandom"]] = relationship(
        back_populates="category", cascade="all, delete-orphan"
    )
    def __repr__(self) -> str:
        return f"Category(id={self.id!r}, label={self.label!r})"


class Fandom(Base):
    __tablename__ = "fandom"
    id: Mapped[int] = mapped_column(primary_key=True)
    label: Mapped[str] = mapped_column(String(255))
    category_id: Mapped[int] = mapped_column(ForeignKey("category.id"))
    category: Mapped["Category"] = relationship(back_populates="fandoms")
    stories: Mapped[Optional[List["Story"]]] = relationship(
        secondary=fandom_story_assoc, back_populates="fandoms"
    )
    def __repr__(self) -> str:
        return f"Fandom(id={self.id!r}, label={self.label!r})"

class Author(Base):
    __tablename__ = "author"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255))
    stories: Mapped[List["Story"]] = relationship(
        back_populates="author", cascade="all, delete-orphan"
    )
    def __repr__(self) -> str:
        return f"Author(id={self.id!r}, name={self.name!r})"


class Story(Base):
    __tablename__ = "story"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(255))
    fandoms: Mapped[List["Fandom"]] = relationship(secondary=fandom_story_assoc, back_populates="stories")
    author_id: Mapped[int] = mapped_column(ForeignKey("author.id"))
    author: Mapped["Author"] = relationship(back_populates="stories")
    def __repr__(self) -> str:
        return f"Story(id={self.id!r}, title={self.title!r}, author={self.author.name!r})"
