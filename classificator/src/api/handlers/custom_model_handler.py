from fastapi import Depends, HTTPException

from classificator.src.api.dependencies.dependencies import get_custom_model, get_labels_service
from classificator.src.api.models.request import ClassificationRequest
from classificator.src.api.models.response import Category
from classificator.src.services.prompt_service import PromptService
from common.src.llm_model.custom_model import CustomModel
from common.src.logging.logger import AppLogger


class CustomModelHandler:
	def __init__(
		self,
		model: CustomModel = Depends(get_custom_model),
		labels_service = Depends(get_labels_service)
	):
		self.model = model
		self.labels_service = labels_service
		self.prompt_service = PromptService()
		self.logger = AppLogger.get_instance().get_logger()

	def classify_article(self, request: ClassificationRequest) -> Category:
		try:
			prompt = self.prompt_service.create_prompt(request.get_text())
			response = self.model.invoke(prompt.format()).strip().lower()
			label = self.labels_service.get_label(response)
			self.logger.info(f'Article classified into category: {label}')
			return Category(category=label)
		except Exception as e:
			self.logger.error(f'Error classifying article: {str(e)}')
			raise HTTPException(status_code=500, detail='Error classifying article')
