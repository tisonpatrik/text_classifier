from fastapi import FastAPI

from classificator.src.api.routes.ollama_router import router as ollama_route
from classificator.src.api.routes.openai_route import router as openai_route
from classificator.src.api.routes.custom_model_router import router as custom_model_route
from common.src.logging.logger import AppLogger

app = FastAPI()
app.include_router(openai_route, prefix='/openai_route')
app.include_router(ollama_route, prefix='/ollama_route')
app.include_router(custom_model_route, prefix='/custom_model_route')
logger = AppLogger.get_instance().get_logger()
logger.info('App started successfully.')
