from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from app.server.database import (
    add_client,
    delete_client,
    retrieve_client,
    retrieve_clients,
    update_client,
)
from app.server.models.client import (
    ErrorResponseModel,
    ResponseModel,
    ClientSchema,
    UpdateClientModel,
)

router = APIRouter()

@router.post("/", response_description="Client data added into the database")
async def add_client_data(client: ClientSchema = Body(...)):
    client = jsonable_encoder(client)
    new_client = await add_client(client)
    return ResponseModel(new_client, "Client added successfully.")
