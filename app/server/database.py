import motor.motor_asyncio
from bson.objectid import ObjectId

MONGO_DETAILS = "mongodb://localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.clients

clients_collection = database.get_collection("Clients_collection")

def client_helper(client) -> dict:
    return {
        "id": str(client["_id"]),
        "fullname": client["fullname"],
        "email": client["email"],
        "service": client["service"],
        "year_of_birth": student["year_of_birth"],
        "rate": student["rate"],
    }


async def retrieve_clients():
    clients = []
    async for client in client_collection.find():
        clients.append(client_helper(client))
    return clients


async def add_client(client_data: dict) -> dict:
    client = await client_collection.insert_one(client_data)
    new_client = await client_collection.find_one({"_id": client.inserted_id})
    return client_helper(new_client)


async def retrieve_client(id: str) -> dict:
    client = await client_collection.find_one({"_id": ObjectId(id)})
    if client:
        return client_helper(client)


async def update_client(id: str, data: dict):
    if len(data) < 1:
        return False
    client = await client_collection.find_one({"_id": ObjectId(id)})
    if client:
        updated_client = await client_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_client:
            return True
        return False


async def delete_client(id: str):
    client = await client_collection.find_one({"_id": ObjectId(id)})
    if client:
        await client_collection.delete_one({"_id": ObjectId(id)})
        return True
