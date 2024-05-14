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

	def create_prompt(self, title, prefix):
		categories_str = ', '.join(self.categories)
		article_input = f'{title} : {prefix}'
		prompt_template = """As an article classifier for a news magazine, determine the appropriate category for this article based on its title and prefix.
        
Title and Prefix: {}
Categories: {}
Choose one of the above categories. If unsure, respond with 'I don't know'.
"""
		return prompt_template.format(article_input, categories_str)
