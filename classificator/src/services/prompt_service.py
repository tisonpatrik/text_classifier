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

	def create_prompt(self, title: str, prefix: str) -> str:
		try:
			if not title or not prefix:
				raise ValueError('Title and prefix must not be empty.')

			categories_str = ', '.join(self.categories)
			article_input = f'{title} : {prefix}'
			prompt_template = """Classify the following article title and prefix into one of the given categories. Respond with one category name only.

Title and Prefix: {0}
Categories: {1}
If unsure, respond with 'I don't know'.
"""
			self.logger.info('Prompt created successfully.')
			return prompt_template.format(article_input, categories_str)
		except ValueError as ve:
			self.logger.error(f'ValueError occurred: {ve}')
			raise
		except Exception as e:
			self.logger.error(f'An unexpected error occurred: {e}')
			raise
