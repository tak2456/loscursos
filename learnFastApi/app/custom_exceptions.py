from fastapi import Request, status
from fastapi.responses import JSONResponse

class MyCustomException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


async def custom_exception_handler(request: Request, exc: MyCustomException):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"message": f"someting is definitely wrong with '{exc.message}'"}
    )