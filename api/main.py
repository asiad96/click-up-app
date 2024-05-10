from fastapi import FastAPI
from dotenv import load_dotenv
import os

load_dotenv()  # This loads the environment variables from the .env file into the environment

API_TOKEN = os.getenv("CLICKUP_API_TOKEN")

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}
