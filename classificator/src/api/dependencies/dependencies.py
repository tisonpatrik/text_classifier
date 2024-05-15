import os

from dotenv import load_dotenv
from langchain_community.llms.ollama import Ollama
from langchain_openai import OpenAI
from pydantic.v1 import SecretStr

from common.src.logging.logger import AppLogger

logger = AppLogger.get_instance().get_logger()


def get_open_ai_model():
	try:
		load_dotenv()
		api_key_env = os.getenv('OPENAI_API_KEY')
		if not api_key_env:
			logger.error('OPENAI_API_KEY environment variable is not set.')
			raise ValueError('OPENAI_API_KEY environment variable is not set.')

		api_key = SecretStr(api_key_env)
		model = OpenAI(api_key=api_key, model='gpt-3.5-turbo-instruct', temperature=0)

		logger.info('Successfully created OpenAI model instance.')
		return model
	except Exception as e:
		logger.error(f'Error occurred while creating OpenAI model: {e}')
		raise


def get_ollama():
	try:
		model = Ollama(model='mistral:instruct', base_url='http://ollama:11434', temperature=0)
		logger.info('Successfully created Ollama model instance.')
		return model
	except Exception as e:
		logger.error(f'Error occurred while creating Ollama model: {e}')
		raise
