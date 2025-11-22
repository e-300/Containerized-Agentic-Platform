# LAYER 3 - API Layer
# Pydantic-> Validates Response message exists, is str and if not returns error prior to code exec
# Request -> validation -> processing -> response   

from fastapi import FastAPI
from pydantic import BaseModel
from agent.claude import AnthropicAgent
import os
from dotenv import load_dotenv

load_dotenv()


class ChatRequest(BaseModel):
    message: str


app = FastAPI()

api_key = os.getenv("ANTHROPIC_API_KEY")

if api_key is None:
    raise ValueError("ANTHROPIC_API_KEY environment variable is missing.")



# Redis configuration from environment variables
redis_host = os.getenv("REDIS_HOST", "redis")
redis_port = int(os.getenv("REDIS_PORT", "6379"))

# Agent initialized with Redis config
agent = AnthropicAgent(
    api_key=api_key, 
    system_prompt=None,
    redis_host=redis_host,
    redis_port=redis_port
)


@app.post("/chat")
async def chat(req: ChatRequest):
    
    response = agent.process(req.message)
    
    return {"response": response}



