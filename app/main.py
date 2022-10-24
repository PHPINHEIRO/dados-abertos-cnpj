from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/{numero}")
async def root2():

    return {"message": "Hello World"}

@app.get("/teste")
async def root3(valor: int):
    return {"message": "Hello World"}
