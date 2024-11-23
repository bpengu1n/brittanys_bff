from sqlalchemy import create_engine
from sqlalchemy.orm import Session

engine = create_engine("sqlite:///test.db", echo=True)

from model import Story


Story.Base.metadata.create_all(engine)

test_story = Story.Story()


with Session(engine) as session:
    session.add(test_story)
    session.commit()