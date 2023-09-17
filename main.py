from fastapi import FastAPI
import uvicorn
from recommand import *
from pydantic import BaseModel


app = FastAPI()
Recommand_module = Recommand()

class In(BaseModel):
    text : str

@app.get('/')
def home():
    return "main"

@app.get('/recommand')
def recommand(data : In):
    global Recommand_module
    return Recommand_module.get_query_sim_top_k(data.text)


if __name__ == "__main__":
    uvicorn.run("main:app" , host="127.0.0.1", port=8000)