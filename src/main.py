from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(title="CRM Integration Service")

class User(BaseModel):
    id: int
    name: str
    email: str

@app.get("/users", response_model=List[User])
async def get_users():
    # Example data
    return [
        {"id": 1, "name": "Иван Иванов", "email": "ivan@example.com"},
        {"id": 2, "name": "Мария Смирнова", "email": "maria@example.com"}
    ]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)