from pydantic import BaseModel, Field


class ClassificationRequest(BaseModel):
	title: str = Field(
		default="""Pastrňákova trefa Bostonu nestačila, Florida je výhru od postupu. Vancouver vede sérii s Edmontonem"""
	)
	prefix: str = Field(
		default="""Český hokejový útočník David Pastrňák dal ve čtvrtém utkání série druhého kola play-off NHL proti Floridě svůj první gól. Boston v domácím zápase vedl 2:0, náskok ale neudržel a prohrál 2:3. Bruins tak dělí jediný duel od vyřazení. Vancouver vyhrál v Edmontonu 4:3 a v sérii se ujal vedení 2:1."""
	)

	def get_text(self) -> str:
		return f'{self.prefix} {self.title}'
