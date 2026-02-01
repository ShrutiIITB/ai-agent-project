from fastapi import FastAPI, HTTPException 
from pydantic import BaseModel
from typing import List 

from app.agent.ai_agent import get_response_from_ai_agents 
from app.config.settings import settings 
from app.utlis.logger import get_logger 
from app.utlis.common_exception import CustomException

logger = get_logger(__name__)

app = FastAPI(title="AI Agent", 
              version="1.0.0")

class QueryRequest(BaseModel):

    model_name : str
    system_prompt : str
    messages: List[str]
    allow_search: bool


@app.post("/chat", summary="Get response from AI agents")
def chat_endpoint(request: QueryRequest):
    logger.info(f"Received chat request with model: {request.model_name}")
    
    if request.model_name not in settings.ALLOWED_MODEL_NAMES:
        logger.warning("Invalid model name")
        raise HTTPException(status_code=400 , detail='Invalid model name')
    
    
    try:
        print(request.messages, request.system_prompt)
        response = get_response_from_ai_agents(
            request.model_name,
            request.messages,
            request.allow_search,
            request.system_prompt
        )
        logger.info(f"Successfully got response from AI Agent {request.model_name}")

        return {
            'response' : response,
            'status_code' : 200
        }
    except Exception as e:
        logger.error(f"Failed to get AI response: {str(e)}")
        raise HTTPException(status_code=500 , 
                            detail= str(CustomException("Failed to get AI response",str(e)))
                            )

if __name__ == "__main__":

    # test AI agent endpoint
    test_request = QueryRequest(
        model_name='gpt-4o-mini',
        system_prompt="You are a geography expert. Answer the user's question directly and concisely with accurate information.",
        messages=["What is the capital of France?"],
        allow_search=True
    )
    response = chat_endpoint(test_request)
    print("Test AI Agent Response:", response)