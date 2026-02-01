from dotenv import load_dotenv 
import os 

# Load env variables 
load_dotenv() 

class Settings:

    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

    ALLOWED_MODEL_NAMES = [ 'gpt-4o-mini',
                           'gpt-3.5-turbo'
    ]

settings = Settings()

if __name__ == "__main__":
    print("Models Allowed:", settings.ALLOWED_MODEL_NAMES)

