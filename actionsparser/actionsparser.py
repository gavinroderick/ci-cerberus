import os.path

from utils import logging

logger = logging.setup_logger(__name__)

class ActionsParser:
    def __init__(self, github_directory: str = ".github/workflows"):
        self.github_directory = os.path.normpath(github_directory)

    def find_workflow_files(self):
        try:
            files = os.listdir(self.github_directory)
            logger.info(f"Found {len(files)} workflows")
            for file in files:
                logger.info(f"    {file}")
            return files
        except FileNotFoundError:
            path = os.path.join(os.getcwd(), self.github_directory)
            logger.error(f"No directory found at {path}")