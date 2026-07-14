import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

try:
    import streamlit as st

    api_key = st.secrets.get(
        "OPENAI_API_KEY",
        os.getenv("OPENAI_API_KEY")
    )

    base_url = st.secrets.get(
        "OPENAI_BASE_URL",
        os.getenv("OPENAI_BASE_URL")
    )

    model_name = st.secrets.get(
        "OPENAI_MODEL",
        os.getenv("OPENAI_MODEL")
    )

except Exception:

    api_key = os.getenv("OPENAI_API_KEY")

    base_url = os.getenv("OPENAI_BASE_URL")

    model_name = os.getenv("OPENAI_MODEL")


llm = ChatOpenAI(

    api_key=api_key,

    base_url=base_url,

    model=model_name,

    temperature=0

)