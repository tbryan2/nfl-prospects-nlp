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


# Gradio app
def greet(query):
    OPENAI_API_KEY = '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'
    PINECONE_API_KEY = '9d924de2-6f86-47cf-8fc1-ff61ef7542ed'
    os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY

    embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)

    pinecone.init(
        api_key=PINECONE_API_KEY,
        environment="northamerica-northeast1-gcp"
    )
    index_name = "nfl-prospects-1"

    llm = OpenAI(temperature=0, openai_api_key=OPENAI_API_KEY)
    chain = load_qa_chain(llm, chain_type="stuff")

    docs = docsearch.similarity_search(query, include_metadata=True)

    return chain.run(input_documents=docs, question=query)


demo = gr.Interface(fn=greet,
                    inputs="text",
                    outputs="text")

demo.launch()
