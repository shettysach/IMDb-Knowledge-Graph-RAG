from os import getenv
from dotenv import load_dotenv
from langchain_community.graphs import Neo4jGraph
from langchain.chains import GraphCypherQAChain
from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st

load_dotenv()

NEO4J_URL = getenv("NEO4J_URL")
NEO4J_USER = getenv("NEO4J_USER")
NEO4J_PASSWORD = getenv("NEO4J_PW")
NEO4J_DATABASE = getenv("NEO4J_DB")
GEMINI_API = getenv("GEMINI_API")


@st.cache_resource
def graph_chain():
    graph = Neo4jGraph(NEO4J_URL, NEO4J_USER, NEO4J_PASSWORD, NEO4J_DATABASE)
    llm = ChatGoogleGenerativeAI(
        model="gemini-pro", google_api_key=GEMINI_API, temperature=0
    )
    chain = GraphCypherQAChain.from_llm(
        graph=graph, llm=llm, return_intermediate_steps=True, verbose=True
    )
    return chain


def infer(chain, prompt):
    response = chain.invoke(prompt)
    query = response["intermediate_steps"][0]["query"]
    context = response["intermediate_steps"][1]["context"]
    result = response["result"]
    return query, context, result


if __name__ == "__main__":
    st.subheader("IMDbot")
    st.write("Made using Neo4j, Langchain and Gemini.")
    chain = graph_chain()

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Ask questions about IMDb's top 250."):
        st.chat_message("user").markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})

        query, context, result = infer(chain, prompt)
        with st.chat_message("assistant"):
            st.code(query, language="cypher")
            st.write(context)
            st.markdown(result)
        st.session_state.messages.append({"role": "assistant", "content": result})
