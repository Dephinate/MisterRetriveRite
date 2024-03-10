from langchain.text_splitter import RecursiveCharacterTextSplitter
class DataSplitter():
    def __init__(self,data) -> None:
        self.data = data
        pass
    def split_recursive(self, chunk_size:int,chunk_overlap:int,sperators:list[str]):
        Splitter = RecursiveCharacterTextSplitter(
            separators=sperators,
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap
        )
        splits = Splitter.split_documents(self.data)
        return splits