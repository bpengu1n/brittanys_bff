from sqlalchemy import create_engine
from sqlalchemy.orm import Session

engine = create_engine("sqlite:///test.db", echo=True)

from model import Story as schema


schema.Base.metadata.create_all(engine)

cat_anime = schema.Category(id=5, label="Anime & Manga")
cat_movies = schema.Category(id=2, label="Movies")

author_test = schema.Author(id=23, name="Jane Doe")
fandom_fma = schema.Fandom(id=1, label="Full Metal Alchemist", category=cat_anime)
fandom_hp = schema.Fandom(id=2, label="Harry Potter", category=cat_movies)

test_stories = (
    schema.Story(id=52, title="test", 
                          fandoms=[fandom_fma], author=author_test),
    schema.Story(id=59, title="test2", 
                          fandoms=[fandom_fma, fandom_hp], author=author_test)
)

with Session(engine) as session:
    session.add_all(test_stories)
    session.commit()