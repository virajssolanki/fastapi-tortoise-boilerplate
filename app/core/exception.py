from fastapi.requests import Request
from fastapi import HTTPException, status
from fastapi.responses import JSONResponse

import traceback
import sys


class APIException(HTTPException):
    '''
    just a HTTPException hook that can be modified if needed. 
    '''
    detail: str = "Server error."
    status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR

    def __init__(self, detail="", status_code=None):
        self.detail = detail or self.detail
        self.status_code = status_code or self.status_code
        super().__init__(status_code=self.status_code, detail=self.detail)


class ConflictException(APIException):
    detail: str = "There was a conflict in database."
    status_code: int = status.HTTP_409_CONFLICT

class BadRequestException(APIException):
    detail: str = "Bad request, check documentation."
    status_code: int = status.HTTP_400_BAD_REQUEST

class AuthenticationFailed(APIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail: str = "Incorrect authentication credentials."

class NotAuthenticated(APIException):
    status_code: int = status.HTTP_401_UNAUTHORIZED
    detail: str = "Authentication credentials were not provided."

class PermissionDenied(APIException):
    status_code: int = status.HTTP_403_FORBIDDEN
    detail: str = 'You do not have permission to perform this action.'


async def http_exception_handler(
    request: Request,
    exception: HTTPException
) -> JSONResponse:

    print(traceback.format_exc())
    print(sys.exc_info())

    content = {
            "data": {},
            "message": str(exception.detail),
            "success": False,
            "status": exception.status_code
    }

    return JSONResponse(content=content, status_code=status.HTTP_200_OK)