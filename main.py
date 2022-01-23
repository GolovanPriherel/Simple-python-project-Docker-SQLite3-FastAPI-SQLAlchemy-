import uvicorn
from fastapi import FastAPI
from src.Database_Utils.DB_Requests import *

DataReq = DatabaseORM()
app = FastAPI()
print('Service is ON')


@app.get("/")
async def root():
    return 'root'


@app.get("/create/")
async def create_database():
    try:
        DataReq.create_tables()
    except Exception as err:
        return err
    return 'OK'


@app.get("/show/")
async def select_databases():
    try:
        response = DataReq.show_tables()
    except Exception as err:
        return err
    return response


@app.get("/insert/")
async def insert_databases():
    try:
        DataReq.insert_tables()
    except Exception as err:
        return err
    return 'Данные успешно загружены'


@app.get("/drop/")
async def drop_databases():
    try:
        response = DataReq.delete_tables()
    except Exception as err:
        return err
    return response


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5001)
