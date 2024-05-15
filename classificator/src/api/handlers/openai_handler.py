from fastapi import Depends, HTTPException
from langchain_core.prompts.prompt import PromptTemplate
from langchain_openai import OpenAI

from classificator.src.api.dependencies.dependencies import get_open_ai_model
from classificator.src.api.models.request import ClassificationRequest
from classificator.src.api.models.response import Category
from classificator.src.services.prompt_service import PromptService
from common.src.logging.logger import AppLogger


class OpenAIHandler:
	def __init__(
		self,
		model: OpenAI = Depends(get_open_ai_model),
	):
		self.model = model
		self.prompt_service = PromptService()
		self.logger = AppLogger.get_instance().get_logger()

	def classify_article(self, request: ClassificationRequest) -> Category:
		try:
			prompt = self.prompt_service.create_prompt(request.title, request.prefix)
			prompt_template = PromptTemplate.from_template(prompt)
			response = self.model.invoke(prompt_template.format()).strip().lower()
			self.logger.info(f'Article classified into category: {response}')
			return Category(category=response)
		except Exception as e:
			self.logger.error(f'Error classifying article: {str(e)}')
			raise HTTPException(status_code=500, detail='Error classifying article')
