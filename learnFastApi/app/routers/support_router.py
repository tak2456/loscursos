import asyncio
from datetime import datetime
from pydantic import Field
from typing import Annotated
from fastapi import Form, Body, Path, Query, File, UploadFile, APIRouter

router = APIRouter(
    prefix="/support",
    tags=["Support"],
    responses={404: {"description": "Not found"}}
)

@router.get("/async-endpoint")
async def async_endpoint():
    print(f"Execution started at {datetime.now()}\n", flush=True)
    await asyncio.sleep(2)
    return {"message": "This is an async endpoint"}


@router.post("/")
async def create_support_ticket(title: Annotated[str, Form()], message: Annotated[str, Form()]):
    return {"title": title, "message": message}