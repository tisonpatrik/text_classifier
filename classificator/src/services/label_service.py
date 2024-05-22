from common.src.logging.logger import AppLogger
import pandas as pd

class LabelsService:
    def __init__(self, labels: pd.DataFrame):
        self.logger = AppLogger.get_instance().get_logger()
        self.labels = labels.set_index('id')

    def get_label(self, label_id: str) -> str:
        try:
            label_id = int(label_id)  # Ensure label_id is an integer
            if label_id in self.labels.index:
                return self.labels.loc[label_id, 'label']
            else:
                self.logger.info(f'Label ID {label_id} not found, returning "Unknown"')
                return 'Unknown'
        except ValueError:
            self.logger.info(f'Invalid label ID {label_id}, returning "Unknown"')
            return 'Unknown'

