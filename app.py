# Dependencies
import gradio as gr
import pandas as pd
import os
import pinecone

from langchain.retrievers import PineconeHybridSearchRetriever
from langchain.vectorstores import Pinecone
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain

from config import openai_api_key, pinecone_api_key

# Gradio app
def question(query):
    OPENAI_API_KEY = openai_api_key
    PINECONE_API_KEY = pinecone_api_key

    embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)

    pinecone.init(
        api_key=PINECONE_API_KEY,
        environment="northamerica-northeast1-gcp"
    )
    index_name = "nfl-prospects-1"

    llm = OpenAI(temperature=0, openai_api_key=OPENAI_API_KEY)
    chain = load_qa_chain(llm, chain_type="stuff")

    docsearch = Pinecone.from_existing_index(index_name, embeddings)

    docs = docsearch.similarity_search(query, include_metadata=True)

    return chain.run(input_documents=docs, question=query)


demo = gr.Interface(fn=question,
                    inputs="text",
                    outputs="text")

demo.launch()
