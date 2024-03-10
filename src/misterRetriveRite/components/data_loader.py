from langchain.document_loaders import UnstructuredURLLoader
from misterRetriveRite.logging import logger
class DataLoader():
    def __init__(self) -> None:
        pass
    def load_from_url(self,urls: list):
        loader = UnstructuredURLLoader(urls=urls)
        data = loader.load()
        logger.info(f"Data loaded from : {urls}")
        return data