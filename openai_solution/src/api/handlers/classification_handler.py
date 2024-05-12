from fastapi import Depends
from langchain_core.prompts.prompt import PromptTemplate
from langchain_openai import OpenAI

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

	def classify_article(self, request: ClassificationRequest):
		prompt = self.prompt_service.create_prompt(request.title, request.prefix)
		prompt_template = PromptTemplate.from_template(prompt)
		response = self.open_ai_model.invoke(prompt_template.format()).strip()
		return Category(category=response)
