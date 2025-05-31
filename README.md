# Langchain Gemini RAG Application

This repository contains a Retrieval Augmented Generation (RAG) application built using **Langchain**, **Google Gemini**, and a **Flask** backend. The application allows you to interact with your documents by leveraging the power of large language models for intelligent retrieval and response generation.

## Project Overview

The project aims to provide a robust and scalable solution for question-answering over custom document sets. Key components and their roles include:

* **Langchain:** A framework for developing applications powered by language models. It's used here for orchestrating the RAG pipeline, including document loading, splitting, embedding, vector store creation, and query processing.
* **Google Gemini:** Google's powerful family of large language models, used for generating coherent and contextually relevant responses based on the retrieved document snippets.
* **Flask:** A lightweight Python web framework that serves as the backend API for the RAG application. It handles incoming user queries and returns the generated responses.
* **ChromaDB (via Langchain-Chroma):** A fast, in-memory vector database used to store embeddings of your documents. This allows for efficient semantic search and retrieval of relevant document chunks.
* **Docker:** Used for containerizing the entire application, ensuring consistent environments, easy deployment, and simplified dependency management. It also facilitates mounting external document directories into the container.

The application workflow typically involves:
1.  **Document Ingestion:** Loading documents (e.g., PDFs, text files) from a specified directory.
2.  **Text Splitting:** Dividing large documents into smaller, manageable chunks.
3.  **Embedding:** Converting these text chunks into numerical vector representations (embeddings) using a model.
4.  **Vector Storage:** Storing these embeddings in ChromaDB for efficient similarity search.
5.  **Query Processing:** When a user submits a query, it's embedded and used to search for the most relevant document chunks in ChromaDB.
6.  **Response Generation:** The retrieved chunks, along with the user's query, are fed to the Google Gemini model to generate a comprehensive and informed answer.

## Project Setup

Follow these instructions to set up and run the Langchain Gemini RAG application locally using Docker.

### Prerequisites

Before you begin, ensure you have the following installed:

* **Python 3.12+:** For running the application code.
* **pip:** Python package installer.
* **Docker:** For building and running the containerized application.
* **Google Gemini API Key:** You'll need an API key to interact with the Gemini models. Obtain one from the [Google AI Studio](https://aistudio.google.com/app/apikey).

### 1. Clone the Repository

First, clone the project repository to your local machine:

```bash
git clone [https://github.com/bilalsohailmirza/langchain-gemini-rag.git](https://github.com/bilalsohailmirza/langchain-gemini-rag.git)
cd langchain-gemini-rag
```

### 2. Prepare Your Documents
Place all your .pdf documents that you want the RAG application to process into a directory named documents within the langchain-gemini-rag project root.

#### Example:
```
langchain-gemini-rag/
├── app.py
├── requirements.txt
├── Dockerfile
└── documents/
    ├── my_report.pdf
    └── company_faq.txt
```
### 3. Install the dependencies
  #### a. using venv (debian/ubuntu, on the OS it might be different)

  ```
   python3 -m venv <path/to/your/venv>
  ```
  ```
   source <path/to/your/venv>/bin/activate
  ```
  ```
   pip install requirements.txt
  ```
  ```
   python3 app.py
  ```

#### b. using docker (debian/ubuntu, on the OS it might be different)

  ```
   docker build . -t <tag_name>
  ```
  ```
   docker run -d -p 5000:5000 --name rag-flask-container \
  -v "$(pwd)/documents":/app/documents \
  -e GEMINI_API_KEY="YOUR_ACTUAL_GEMINI_API_KEY" \
  langchain-gemini-rag-app
  ```
