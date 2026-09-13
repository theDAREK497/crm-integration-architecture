from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="CRM Integration Service")


class User(BaseModel):
    id: int
    name: str
    email: str


@app.get("/users", response_model=list[User])
async def get_users() -> list[User]:
    return [
        User(id=1, name="Иван Иванов", email="ivan@example.com"),
        User(id=2, name="Мария Смирнова", email="maria@example.com"),
    ]


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
