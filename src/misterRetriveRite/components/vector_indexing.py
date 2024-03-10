from langchain.vectorstores import FAISS
from misterRetriveRite.utils.common import pickel_dump
import os

class Vectorizer():
    def __init__(self,data_splits) -> None:
        self.data_splits = data_splits
    def build_vectorindex_with_faiss_and_openai(self, save_to_local:bool,file_dir:None,file_name:None):
        from langchain.embeddings import OpenAIEmbeddings
        embeddings = OpenAIEmbeddings()
        vectorindex = FAISS.from_documents(self.data_splits, embeddings)
        if save_to_local:
            file_path = os.path.join(file_dir,file_name)
            pickel_dump(file_path=file_path,data=vectorindex)
            return vectorindex
        return vectorindex
    
    def build_vectorindex_with_faiss_and_huggingface(self, model_name: str,save_to_local:bool,file_dir:None,file_name:None):
        from langchain.embeddings.huggingface import HuggingFaceBgeEmbeddings
        embeddings = HuggingFaceBgeEmbeddings(model_name = model_name)
        vectorindex = FAISS.from_documents(self.data_splits, embeddings)
        if save_to_local:
            file_path = os.path.join(file_dir,file_name)
            pickel_dump(file_path=file_path,data=vectorindex)
            return vectorindex
        return vectorindex