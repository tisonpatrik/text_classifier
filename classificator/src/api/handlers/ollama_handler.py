from fastapi import Depends, HTTPException
from langchain_community.llms.ollama import Ollama

from classificator.src.api.dependencies.dependencies import get_ollama
from classificator.src.api.models.request import ClassificationRequest
from classificator.src.api.models.response import Category
from classificator.src.services.prompt_service import PromptService
from common.src.logging.logger import AppLogger


class OllamaHandler:
	def __init__(
		self,
		model: Ollama = Depends(get_ollama),
	):
		self.model = model
		self.prompt_service = PromptService()
		self.logger = AppLogger.get_instance().get_logger()

	def classify_article(self, request: ClassificationRequest) -> Category:
		try:
			prompt = self.prompt_service.create_prompt(request.get_text())
			response = self.model.invoke(prompt.format()).strip().lower()
			self.logger.info(f'Article classified into category: {response}')
			return Category(category=response)
		except Exception as e:
			self.logger.error(f'Error classifying article: {str(e)}')
			raise HTTPException(status_code=500, detail='Error classifying article')
