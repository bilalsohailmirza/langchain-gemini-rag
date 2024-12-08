import os
from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

def load_data():
    loader = PyPDFLoader("what-makes-a-great-software-engineer.pdf")
    data = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 1000)
    docs = text_splitter.split_documents(data)

    return docs

# print(type(docs))
# def create_embeddings():
#     embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=os.environ['GOOGLE_API_KEY'])


def create_vector_store(docs):
    vector_store = Chroma.from_documents(
        documents=docs,
        embedding=GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    )

    return vector_store


def retrieve_docs(vector_store, input):
    retriever = vector_store.as_retriever(search_type='similarity', search_kwargs={"k": 10})
    retrieved_docs = retriever.invoke(input)

    return retriever, retrieved_docs
    # len(retrieved_docs)
# for retrieved_doc in retrieved_docs:
#     print(retrieved_doc.page_content)



llm = ChatGoogleGenerativeAI(model='gemini-1.5-flash', temprature=0.3, max_tokens=1000)

system_prompt = (
    "You are an assistant for answering questions. "
    "Use the following pieces of retrieved context to answer the question. "
    "If you don't know the answer, say that you don't know."
    "Keep your answers comprehensive & detailed and format your answer in bullet points."
    "\n\n"
    "{context}"
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}"),
    ]
)

documents = load_data()
vector_store = create_vector_store(documents)

# user_input = input("Enter your prompt: ")
# retriever, retrieved_docs = retrieve_docs(vector_store, user_input)


question_answer_chain = create_stuff_documents_chain(llm, prompt)
# rag_chain = create_retrieval_chain(retriever, question_answer_chain)

# response = rag_chain.invoke({"input": user_input})

# print(response["answer"])


# if __name__ == '__main__':
#     main()
