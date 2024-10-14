from datetime import datetime
from pydantic import BaseModel, Field
from typing import Union, Optional, Annotated
from fastapi import FastAPI, Form, HTTPException, Body, Path, Query, File, UploadFile, APIRouter, status

from app.database import DB_DEPENDENCY
from app.models.todo_model import Todo
from app.schemas.todo_schema import TodoSchema
from app.custom_exceptions import MyCustomException


router = APIRouter(
 #   prefix="/todo"
 tags = ["Todo"],
)

TODO_LIST = [
    {"id": 1, "title": "Todo 1", "description": "This is a description of Todo 1", "complete": False},
    {"id": 2, "title": "Todo 2", "description": "This is a description of Todo 2", "complete": True},
    {"id": 3, "title": "Todo 3", "description": "This is a description of Todo 3", "complete": False},
    {"id": 4, "title": "Todo 4", "description": "This is a description of Todo 4", "complete": True},
]


# class Todo(BaseModel):
#     id: Optional[int] = None
#     title: str
#     description: str = Field(min_length=5, max_length=100)
#     complete: bool = Field(default=False)


# @router.get("/todo")
# async def get_all(completion: bool = None):
#     filtered_todos = list(filter(lambda todo: todo["complete"] == completion if completion is not None else True, TODO_LIST))
#     return filtered_todos

@router.get("/todo", status_code=status.HTTP_200_OK)
async def get_all(db:DB_DEPENDENCY):
    return db.query(Todo).all()


@router.get("/todo/{todo_id}")
async def get_one(todo_id: int):
    try: 
        todo = next((todo for todo in TODO_LIST if todo["id"] == todo_id))
        return todo
    except:
        # raise HTTPException(
        #     status_code=404, 
        #     detail=f"Todo Item {todo_id} not found",
        #     headers={"X-Error": "There goes my error"}
        #     )
        raise MyCustomException(message=f"Todo Item {todo_id} not found")
    
# @app.post("/todo")    
# async def create_todo(id: int = Body(), title: str = Body(), description: str = Body(), complete: bool= Body()):
#     new_todo = {"id": id, "title": title, "description": description, "complete": complete}
#     TODO_LIST.append(new_todo)
#     return new_todo

# @router.post("/todo", response_model=Todo, name="Create Todo", description="Create a new Todo Item", summary="Create a Todo Element",
#           deprecated=False)     
# async def create_todo(data: Todo):
#     TODO_LIST.append(data)
#     return data

@router.post("/todo/", status_code=status.HTTP_201_CREATED)
async def create_todo(db: DB_DEPENDENCY, todo_request: TodoSchema):
    todo_model = Todo(**todo_request.model_dump())
    db.add(todo_model)
    db.commit()
    db.refresh(todo_model)
    return todo_model



@router.post("/todo/{todo_id}/attachment")
async def upload_attachment(todo_id: Annotated[int, Path()], file: UploadFile):
    try:
        todo_data = next((todo for todo in TODO_LIST if todo["id"] == todo_id))
        #todo_data["file_size"] = len(file)
        todo_data["file_name"] = file.filename
        file_content = await file.read()
        return todo_data
    except:
        return HTTPException(status_code=404, detail=f"Todo Item {todo_id} not found")