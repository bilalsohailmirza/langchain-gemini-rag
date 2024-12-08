from flask import Flask, jsonify, request
from flask_cors import CORS
# from bson.objectid import ObjectId
# from bson.json_util import dumps

from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from chatbot import llm, prompt, vector_store, retrieve_docs

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET'])
def welcome():
    return "Welcome you are accessing the REST API!"


@app.route('/user-query', methods=['GET'])
def retrieve_query():
    data = request.json
    if not data["query"]:
        return jsonify({"error": "User prompt is required."}), 400
        # author_id = authors_collection.insert_one({"name": data["name"]}).inserted_id

    retriever, retrieved_docs = retrieve_docs(vector_store, data["query"])
    question_answer_chain = create_stuff_documents_chain(llm, prompt)
    rag_chain = create_retrieval_chain(retriever, question_answer_chain)
    response = rag_chain.invoke({"input": data["query"]})

    return jsonify(response["answer"])


if __name__ == '__main__':
    app.run(debug=True)
