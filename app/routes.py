from fastapi import APIRouter
from utils.chatbot import chatbot_response
import platform
import os

# from pydantic import BaseModel


router = APIRouter()


@router.get("/")
async def index():
    return {
        "message": "Hello World! This is the chatbot API. Please use the /chatbot endpoint to get a response from the chatbot.",
        "debug": {
            "OSPlatform": platform.system(),
            "OSArch": platform.machine(),
            "OSProcessor": platform.processor(),
            "OSName": os.name,
        },
    }


@router.post("/chatbot")
async def chatbot(text: str):
    return {"message": chatbot_response(text)}
