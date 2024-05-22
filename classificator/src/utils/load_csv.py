import pandas as pd
from common.src.logging.logger import AppLogger

logger = AppLogger.get_instance().get_logger()

def load_csv(file_path: str) -> pd.DataFrame:
    try:
        labels = pd.read_csv(file_path)
        return labels
    except Exception as e:
        logger.error(f'Error loading labels: {str(e)}')
    return labels