import os

from dotenv import load_dotenv
from langchain_community.llms.ollama import Ollama
from langchain_openai import OpenAI
from pydantic.v1 import SecretStr
from classificator.src.services.label_service import LabelsService
from classificator.src.utils.load_csv import load_csv
from common.src.llm_model.custom_model import CustomModel
from common.src.logging.logger import AppLogger

logger = AppLogger.get_instance().get_logger()
load_dotenv()


def get_open_ai_model():
	try:
		api_key_env = os.getenv('OPENAI_API_KEY')
		if not api_key_env:
			raise ValueError('OPENAI_API_KEY environment variable is not set.')

		api_key = SecretStr(api_key_env)
		open_ai_model = os.getenv('OPENAI_MODEL')
		model = OpenAI(api_key=api_key, model=open_ai_model, temperature=0)

		logger.info('Successfully created OpenAI model instance.')
		return model
	except Exception as e:
		logger.error(f'Error occurred while creating OpenAI model: {e}')
		raise


def get_ollama():
	try:
		ollama_model = os.getenv('OLLAMA_MODEL')
		logger.debug(f'OLLAMA_MODEL value: {ollama_model}')
		if ollama_model is None:
			raise ValueError("OLLAMA_MODEL environment variable not set")
		model = Ollama(model=ollama_model, base_url='http://ollama:11434', temperature=0)
		logger.info('Successfully created Ollama model instance.')
		return model
	except Exception as e:
		logger.error(f'Error occurred while creating Ollama model: {e}')
		raise

def get_custom_model():
    try:
        custom_model = os.getenv('CUSTOM_MODEL')
        logger.debug(f'CUSTOM_MODEL value: {custom_model}')
        if custom_model is None:
            raise ValueError("CUSTOM_MODEL environment variable not set")
        model = CustomModel(model_name=custom_model)
        logger.info('Successfully created CustomModel instance.')
        return model
    except Exception as e:
        logger.error(f'Error occurred while creating CustomModel: {e}')
        raise



def get_labels_service():
	try:
		labels_file = os.getenv('LABELS_FILE')
		labels = load_csv(labels_file)
		logger.info('Successfully loaded labels.')
		return LabelsService(labels)
	except Exception as e:
		logger.error(f'Error occurred while loading labels: {e}')
		raise