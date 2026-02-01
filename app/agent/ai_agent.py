from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch
from langchain.messages import AIMessage
from langchain.agents import create_agent 
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

from app.config.settings import settings 

def get_response_from_ai_agents(llm_id, query, allow_search, system_prompt):

    llm = ChatOpenAI(model=llm_id,
                     temperature=0.7,
                     api_key=settings.OPENAI_API_KEY) 

    
    tools = [TavilySearch(api_key=settings.TAVILY_API_KEY, max_results=2)] if allow_search else [] 

    # Create a proper prompt template with system prompt
    

    agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt=system_prompt,
    )
    result = agent.invoke({
        "messages": [
            {"role": "user", "content": query[0]}
        ]
    })

    # Extract the final AI message
    for msg in reversed(result["messages"]):
        if isinstance(msg, AIMessage):
            return msg.content


if __name__ == "__main__":
    response = get_response_from_ai_agents(
        llm_id= 'gpt-4o-mini',
        query= ["Who is the president of the United States?"],
        allow_search= True,
        system_prompt= "You are a helpful AI assistant."
    )

    print("AI Response:", type(response), response)


