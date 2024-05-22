from common.src.logging.logger import AppLogger
import pandas as pd

class LabelsService:
    def __init__(self, labels: pd.DataFrame):
        self.logger = AppLogger.get_instance().get_logger()
        self.labels = labels

    def get_label(self, label_id: str) -> str:
        if label_id in self.labels:
            return self.labels[label_id]
        else:
            self.logger.info(f'Label ID {label_id} not found, returning "Unknown"')
            return 'Unknown'