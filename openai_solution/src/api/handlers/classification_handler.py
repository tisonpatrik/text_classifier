from fastapi import Depends, HTTPException
from langchain_core.prompts.prompt import PromptTemplate
from langchain_openai import OpenAI

from common.src.logging.logger import AppLogger
from openai_solution.src.api.dependencies.dependencies import get_open_ai_model
from openai_solution.src.api.models.request import ClassificationRequest
from openai_solution.src.api.models.response import Category
from openai_solution.src.services.prompt_service import PromptService


class ClassificationHandler:
	def __init__(
		self,
		open_ai_model: OpenAI = Depends(get_open_ai_model),
	):
		self.open_ai_model = open_ai_model
		self.prompt_service = PromptService()
		self.logger = AppLogger.get_instance().get_logger()

	def classify_article(self, request: ClassificationRequest) -> Category:
		try:
			prompt = self.prompt_service.create_prompt(request.title, request.prefix)
			prompt_template = PromptTemplate.from_template(prompt)
			response = self.open_ai_model.invoke(prompt_template.format()).strip().lower()
			self.logger.info(f'Article classified into category: {response}')
			return Category(category=response)
		except Exception as e:
			self.logger.error(f'Error classifying article: {str(e)}')
			raise HTTPException(status_code=500, detail='Error classifying article')
