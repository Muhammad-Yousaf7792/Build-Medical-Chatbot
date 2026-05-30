

from flask import Flask, render_template, request
from dotenv import load_dotenv
# from langchain_pinecone import PineconeVectorStore
from langchain_groq import ChatGroq
# from langchain.chains import create_retrieval_chain
# from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

# from src.helper import download_hugging_face_embeddings
from src.prompt import system_prompt

import os



load_dotenv()


# os.environ["PINECONE_API_KEY"] = os.getenv("PINECONE_API_KEY", "")
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY", "")



app = Flask(__name__)



# embeddings = download_hugging_face_embeddings()



# docsearch = PineconeVectorStore.from_existing_index(
#     index_name="medicalchatbot",
#     embedding=embeddings
# )



# retriever = docsearch.as_retriever(
#     search_type="similarity",
#     search_kwargs={"k": 3}
# )



llm = ChatGroq(
    model_name="llama-3.1-8b-instant"
)



prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}")
    ]
)



# question_answer_chain = create_stuff_documents_chain(
#     llm,
#     prompt
# )



# rag_chain = create_retrieval_chain(
#     retriever,
#     question_answer_chain
# )



@app.route("/")
def index():
    return render_template("chat.html")



@app.route("/get", methods=["POST"])
def chat():

    user_message = request.form["msg"]

    # response = rag_chain.invoke({
    #     "input": user_message

    response = llm.invoke(user_message)

    return response.content



if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8080,
        debug=True
    )

