from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class ClientSchema(BaseModel):
    fullname: str = Field(...)
    email: EmailStr = Field(...)
    service: str = Field(...)
    year_of_birth: int = Field(..., gt=1900, lt=2022)
    rate: float = Field(..., gt=0.0)

    class Config:
        schema_extra = {
            "example": {
                "fullname": "Anna Mary",
                "email": "ann@gmail.com",
                "service": "Massage (body)",
                "year_of_birth": 1993,
                "rate": "10.0",
            }
        }


class UpdateClientModel(BaseModel):
    fullname: Optional[str]
    email: Optional[EmailStr]
    service: Optional[str]
    year_of_birth: Optional[int]
    rate: Optional[float]

    class Config:
        schema_extra = {
            "example": {
                "fullname": "Anna Mary",
                "email": "ann@gmail.com",
                "service": "Massage (body)",
                "year_of_birth": 1993,
                "rate": "10.0",            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
