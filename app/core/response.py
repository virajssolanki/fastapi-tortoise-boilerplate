from pydantic import BaseModel


def get_response_model(schema):

    class Schema(BaseModel):
        data: schema
        message: str
        success: bool
        status: int

    return Schema


class ResponseInfo:
    
    def __init__(self, data, message, success, status):
        self.data = data
        self.message = message
        self.success = success
        self.status = status

    def success_payload(self):
        temp_custom_success = {
            "data": self.data,
            "message": self.message,
            "success": self.success,
            "status": self.status
        }
        return temp_custom_success