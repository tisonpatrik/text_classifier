from fastapi import Depends, HTTPException
from langchain_community.llms.ollama import Ollama
from langchain_core.prompts.prompt import PromptTemplate

from classificator.src.api.dependencies.dependencies import get_ollama
from classificator.src.api.models.request import ClassificationRequest
from classificator.src.api.models.response import Category
from classificator.src.services.prompt_service import PromptService
from common.src.logging.logger import AppLogger


class OllamaHandler:
	def __init__(
		self,
		open_ai_model: Ollama = Depends(get_ollama),
	):
		self.open_ai_model = open_ai_model
		self.prompt_service = PromptService()
		self.logger = AppLogger.get_instance().get_logger()

	def classify_article(self, request: ClassificationRequest) -> Category:
		try:
			prompt = self.prompt_service.create_prompt(request.title, request.prefix)
			prompt_template = PromptTemplate.from_template(prompt).format()
			print(prompt_template)
			response = self.open_ai_model.invoke(prompt_template).strip().lower()
			self.logger.info(f'Article classified into category: {response}')
			return Category(category=response)
		except Exception as e:
			self.logger.error(f'Error classifying article: {str(e)}')
			raise HTTPException(status_code=500, detail='Error classifying article')
