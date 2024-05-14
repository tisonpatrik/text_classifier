import os

from dotenv import load_dotenv
from langchain_community.llms.ollama import Ollama
from langchain_openai import OpenAI
from pydantic.v1 import SecretStr


def get_open_ai_model():
	load_dotenv()
	api_key_env = os.getenv('OPENAI_API_KEY')
	api_key = SecretStr(api_key_env) if api_key_env else None
	if api_key is None:
		raise ValueError('OPENAI_API_KEY environment variable is not set.')
	return OpenAI(api_key=api_key, model='gpt-3.5-turbo-instruct', temperature=0.2)


def get_ollama():
	return Ollama(model='phi3:mini')
