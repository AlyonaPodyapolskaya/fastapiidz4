from fastapi import FastAPI
from public.employees import employees_router #, init_db



app = FastAPI()



app.include_router(employees_router)




if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8001)
