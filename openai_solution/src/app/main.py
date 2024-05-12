from fastapi import FastAPI

from common.src.logging.logger import AppLogger
from openai_solution.src.api.routes.classification_route import router as classification_route

app = FastAPI()
app.include_router(classification_route, prefix='/classification_route')
logger = AppLogger.get_instance().get_logger()
