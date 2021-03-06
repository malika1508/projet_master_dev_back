
from fastapi.applications import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.router import pos, animateur, auth, visit
from app.database import engine
import app.models as models


app = FastAPI()

models.Base.metadata.create_all(bind=engine)


app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
## uvicorn main:app --reload
@app.get("/")
async def root():
    return {"message": "Hello World"}
    

app.include_router(pos.router)
app.include_router(auth.router)
app.include_router(animateur.router)
app.include_router(visit.router)
