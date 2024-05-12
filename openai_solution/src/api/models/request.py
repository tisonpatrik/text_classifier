from pydantic import BaseModel


class ClassificationRequest(BaseModel):
	title: str
	prefix: str
