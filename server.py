import os
from dotenv import load_dotenv
load_dotenv()
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from fastapi import FastAPI
from langserve import add_routes

groq_api_key=os.getenv("GROQ_API_KEY")

model = ChatGroq(api_key=groq_api_key)

prompt_template = ChatPromptTemplate([
    ("system" , "Translate into the {language}"),
    ("user" , "{text}")
])

parser = StrOutputParser()

chain = prompt_template | model | parser

app = FastAPI()

add_routes(
    app,
    chain,
    path="/chain"
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

