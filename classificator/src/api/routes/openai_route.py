from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import ValidationError

from classificator.src.api.handlers.openai_handler import OpenAIHandler
from classificator.src.api.models.request import ClassificationRequest
from common.src.logging.logger import AppLogger

router = APIRouter()
logger = AppLogger.get_instance().get_logger()


@router.post(
	'/classify_article/',
	status_code=status.HTTP_200_OK,
	name='classify_article',
)
def get_subsystem_position_for_instrument(
	request: ClassificationRequest = Depends(),
	handler: OpenAIHandler = Depends(),
):
	try:
		category = handler.classify_article(request)
		return category
	except HTTPException as e:
		logger.error(f'An error occurred while trying to run simulation. Error: {e.detail}')
		return {'error': e.detail, 'status_code': e.status_code}
	except ValidationError as e:
		logger.error(f'Validation error for simulation. Error: {e.json()}')
		return {'error': 'Validation error', 'details': e.errors(), 'status_code': status.HTTP_422_UNPROCESSABLE_ENTITY}
