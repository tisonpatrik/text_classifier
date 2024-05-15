from langchain_core.prompts import PromptTemplate

from common.src.logging.logger import AppLogger


class PromptService:
	def __init__(self):
		self.categories = [
			'atletika',
			'baseball',
			'basketbal',
			'biatlon',
			'box',
			'cyklistika',
			'dostihy',
			'florbal',
			'formule1',
			'fotbal',
			'futsal',
			'golf',
			'hazena',
			'hokej',
			'hokejbal',
			'krasobrusleni',
			'lyze_snowboard',
			'moto',
			'olympijske_hry',
			'rugby',
			'rychlobrusleni',
			'tenis',
			'vodni_sporty',
			'volejbal',
		]
		self.logger = AppLogger.get_instance().get_logger()
		self.template = """
		system: Jsi expertní algoritmus pro klasifikaci článků.
        Tvým jediným úkolem je přiřadit textu jednu hodnotu 'Ketegorie' z daného seznamu.
        Jediná možná odpověď je jedna z položek z daného seznamu kategorií.
		Nikdy nevysvětluj, proč jsi vybral danou kategorii.
        kategorie: {categories}
        text: {input_text}
		ODPOVĚZ POUZE JEDNOU KATEGORIÍ ZE SEZNAMU."""

	def create_prompt(self, input_text: str) -> PromptTemplate:
		categories_str = ', '.join(self.categories)
		formatted_template = self.template.format(categories=categories_str, input_text=input_text)

		try:
			prompt = PromptTemplate.from_template(formatted_template)
			self.logger.info('Prompt created successfully.')
			return prompt
		except ValueError as ve:
			self.logger.error(f'ValueError occurred: {ve}')
			raise
		except Exception as e:
			self.logger.error(f'An unexpected error occurred: {e}')
			raise
