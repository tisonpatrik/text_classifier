from langchain_core.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

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
		self.prompt_template = ChatPromptTemplate.from_messages(
			[
				(
					'system',
					"You are an expert extraction algorithm. Only extract relevant information from the text. If you do not know the value of an attribute asked to extract, return null for the attribute's value.",
				),
				MessagesPlaceholder('examples'),
				('human', '{text}'),
			]
		)
		self.examples = [
			('Football championship in Brazil attracts thousands of fans.', 'fotbal'),
			('Serena Williams wins another tennis grand slam.', 'tenis'),
			('Formula 1 race in Monaco was thrilling.', 'formule1'),
		]

	def create_prompt(self, title: str, prefix: str) -> str:
		if not title or not prefix:
			self.logger.error('Title and prefix must not be empty.')
			raise ValueError('Title and prefix must not be empty.')

		categories_str = ', '.join(self.categories)
		article_input = f'{title} : {prefix}'

		try:
			prompt = self.prompt_template.invoke(
				{
					'text': article_input,
					'examples': [HumanMessage(content=ex[0]) for ex in self.examples],
					'categories': categories_str,
				}
			)
			self.logger.info('Prompt created successfully.')
			return prompt.to_string()
		except ValueError as ve:
			self.logger.error(f'ValueError occurred: {ve}')
			raise
		except Exception as e:
			self.logger.error(f'An unexpected error occurred: {e}')
			raise
