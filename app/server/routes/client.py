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

@router.get("/", response_description="Clients retrieved")
async def get_clients():
    clients = await retrieve_clients()
    if clients:
        return ResponseModel(clients, "Clients data retrieved successfully")
    return ResponseModel(clients, "Empty list returned")


@router.get("/{id}", response_description="Client data retrieved")
async def get_client_data(id):
    client = await retrieve_client(id)
    if client:
        return ResponseModel(client, "Client data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "Client doesn't exist.")
