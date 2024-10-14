from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base


class Todo(Base):
    __tablename__ = "todo"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    priority = Column(Integer)
    complete = Column(Boolean, default=False)

    def __repr__(self):
        return f"<Todo(id={self.id}, title={self.title})>"