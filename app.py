 # from flask import Flask, render_template, request  # type: ignore
 # from src.helper import download_hugging_face_embeddings
 # from langchain_pinecone import PineconeVectorStore  # type: ignore
 # from langchain_groq import ChatGroq  # type: ignore
 # from langchain.chains import create_retrieval_chain  # type: ignore
 # from langchain.chains.combine_documents import create_stuff_documents_chain  # type: ignore
 # from langchain_core.prompts import ChatPromptTemplate  # type: ignore
 # from dotenv import load_dotenv  # type: ignore
 # from src.prompt import *
 # import os


 # app = Flask(__name__)
 # Load environment variables
 # load_dotenv()

 # Get API keys from .env
 # PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
 # GROQ_API_KEY = os.getenv("GROQ_API_KEY")

 # Set environment variables
 # os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY if PINECONE_API_KEY else ""
 # os.environ["GROQ_API_KEY"] = GROQ_API_KEY if GROQ_API_KEY else ""

# Download embeddings
# embeddings = download_hugging_face_embeddings()

# Your Pinecone index name
# index_name = "index-name"

# Connect to existing Pinecone index
# docsearch = PineconeVectorStore.from_existing_index(
#     index_name="medicalchatbot",
#     embedding=embeddings
# )

# Create retriever
# retriever = docsearch.as_retriever(
#     search_type="similarity",
#     search_kwargs={"k": 3}
# )

# Initialize Groq LLM
# chatModel = ChatGroq(
#     model_name="llama3-8b-8192"
# )

# Prompt template
# prompt = ChatPromptTemplate.from_messages(
#     [
#         ("system", system_prompt),
#         ("human", "{input}"),
#     ]
# )
# Create chains
# question_answer_chain = create_stuff_documents_chain(
#     chatModel,
#     prompt
# )

# rag_chain = create_retrieval_chain(
#     retriever,
#     question_answer_chain
# )

# Home route
# @app.route("/")
# def index():
#     return render_template("chat.html")

# Chat route
# @app.route("/get", methods=["GET", "POST"])
# def chat():
#     msg = request.form["msg"]
#     input = msg
#     print(input)
#     response = rag_chain.invoke({
#         "input": msg
#     })

#     print("Response:", response["answer"])
#     return str(response["answer"])
    

# Run app
# if __name__ == '__main__':
#     app.run(
#         host="0.0.0.0",
#         port=8080,
#         debug=True
#     )


# from flask import Flask, render_template, request  # type: ignore
# from src.helper import download_hugging_face_embeddings
# from langchain_pinecone import PineconeVectorStore  # type: ignore
# from langchain_groq import ChatGroq  # type: ignore
# from langchain.chains import create_retrieval_chain  # type: ignore
# from langchain.chains.combine_documents import create_stuff_documents_chain  # type: ignore
# from langchain_core.prompts import ChatPromptTemplate  # type: ignore
# from dotenv import load_dotenv  # type: ignore
# from src.prompt import *
# import os

# app = Flask(__name__)

# # Load environment variables
# load_dotenv()

# # Get API keys from .env
# PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
# GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# # Debug API Keys
# print("PINECONE_API_KEY:", PINECONE_API_KEY)
# print("GROQ_API_KEY:", GROQ_API_KEY)

# # Set environment variables
# os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY if PINECONE_API_KEY else ""
# os.environ["GROQ_API_KEY"] = GROQ_API_KEY if GROQ_API_KEY else ""

# # Download embeddings
# print("Loading embeddings...")
# embeddings = download_hugging_face_embeddings()
# print("Embeddings loaded successfully")

# # Connect Pinecone Index
# try:
#     print("Connecting to Pinecone...")
    
#     docsearch = PineconeVectorStore.from_existing_index(
#         index_name="medicalchatbot",
#         embedding=embeddings
#     )

#     print("Pinecone connected successfully")

# except Exception as e:
#     print("PINECONE ERROR:", str(e))

# # Create Retriever
# retriever = docsearch.as_retriever(
#     search_type="similarity",
#     search_kwargs={"k": 3}
# )

# # Initialize Groq Model
# try:
#     print("Initializing Groq Model...")

#     chatModel = ChatGroq(
#     groq_api_key=GROQ_API_KEY,
#     model_name="llama-3.1-8b-instant"
# )
    

#     print("Groq Model Loaded Successfully")

# except Exception as e:
#     print("GROQ ERROR:", str(e))

# # Prompt Template
# prompt = ChatPromptTemplate.from_messages(
#     [
#         ("system", system_prompt),
#         ("human", "{input}"),
#     ]
# )

# # Create QA Chain
# question_answer_chain = create_stuff_documents_chain(
#     chatModel,
#     prompt
# )

# # Create RAG Chain
# rag_chain = create_retrieval_chain(
#     retriever,
#     question_answer_chain
# )

# # Home Route
# @app.route("/")
# def index():
#     return render_template("chat.html")

# # Chat Route
# @app.route("/get", methods=["POST"])
# def chat():

#     try:
#         msg = request.form["msg"]

#         print("\n========================")
#         print("USER MESSAGE:", msg)
#         print("========================\n")

#         # Invoke RAG Chain
#         response = rag_chain.invoke({
#             "input": msg
#         })

#         print("\n========================")
#         print("FULL RESPONSE:", response)
#         print("========================\n")

#         # Extract answer safely
#         answer = response.get("answer", "Sorry, no response generated.")

#         print("\nBOT RESPONSE:", answer)

#         return str(answer)

#     except Exception as e:

#         print("\n=========== ERROR ===========")
#         print(str(e))
#         print("=============================\n")

#         return f"Error: {str(e)}"

# # Run Flask App
# if __name__ == '__main__':

#     app.run(
#         host="0.0.0.0",
#         port=8080,
#         debug=True
#     )

from flask import Flask, render_template, request
from dotenv import load_dotenv
from langchain_pinecone import PineconeVectorStore
from langchain_groq import ChatGroq
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

from src.helper import download_hugging_face_embeddings
from src.prompt import system_prompt

import os


# Load environment variables
load_dotenv()

# API Keys
os.environ["PINECONE_API_KEY"] = os.getenv("PINECONE_API_KEY", "")
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY", "")


# Flask App
app = Flask(__name__)


# Load Embeddings
embeddings = download_hugging_face_embeddings()


# Connect Pinecone
docsearch = PineconeVectorStore.from_existing_index(
    index_name="medicalchatbot",
    embedding=embeddings
)


# Retriever
retriever = docsearch.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 3}
)


# Groq Model
llm = ChatGroq(
    model_name="llama-3.1-8b-instant"
)


# Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}")
    ]
)


# QA Chain
question_answer_chain = create_stuff_documents_chain(
    llm,
    prompt
)


# RAG Chain
rag_chain = create_retrieval_chain(
    retriever,
    question_answer_chain
)


# Home Page
@app.route("/")
def index():
    return render_template("chat.html")


# Chat API
@app.route("/get", methods=["POST"])
def chat():

    user_message = request.form["msg"]

    response = rag_chain.invoke({
        "input": user_message
    })

    return response["answer"]


# Run Server
if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8080,
        debug=True
    )