import streamlit as st
## Session States
if  'urls' not in st.session_state:
    st.session_state['urls'] = False

if  'url_processing' not in st.session_state:
    st.session_state['url_processing'] = False

if  'url_processed' not in st.session_state:
    st.session_state['url_processed'] = False
## Session States snd here
    
## Import Modules 
from misterRetriveRite.utils.common import *
from misterRetriveRite.config.configurations import ConfigurationManager
from misterRetriveRite.components.data_loader import DataLoader
from misterRetriveRite.components.data_splitter import DataSplitter
from misterRetriveRite.components.vector_indexing import Vectorizer
from misterRetriveRite.utils.common import load_env
from langchain import OpenAI
from langchain.chains import RetrievalQAWithSourcesChain
# To_do
load_env("")
## Import modules ends here

## Configurations
config = ConfigurationManager()
vectorization_config = config.get_vectorization_config()
model_config = config.get_model_config()
llm = OpenAI(model=model_config.model_name,temperature=model_config.temperature, max_tokens=model_config.max_tokens)
## Configurations Ends here

## Layout
st.title(":orange[Mr. Retrive Rite] :sunglasses:")
st.markdown("How can I help you today ?")
st.sidebar.title("Paste your URLs Here")
main_placeholder = st.empty()
query = main_placeholder.text_input("Query ................. :mag: ")

# url inputs
url_1 = st.sidebar.text_input(label="URL 1")
url_2 = st.sidebar.text_input(label="URL 2")
url_3 = st.sidebar.text_input(label="URL 3")

## Layout ends here ..

## Process URLs
if url_1 or url_2 or url_3:
    st.session_state.urls = True

# Update State
process_urls = st.sidebar.button("Process URLs :rocket:")

if process_urls:
    st.session_state.url_processing = process_urls

if st.session_state.url_processing:
    if st.session_state.urls:
        # 1 Load data from URLs
        data_loader = DataLoader()
        data = data_loader.load_from_url(urls=[url_1,url_2,url_3])    
        
        # 2 Split data
        splitter = DataSplitter(data=data)
        splits_rec = splitter.split_recursive(
            chunk_size=model_config.chunk_size,chunk_overlap=model_config.chunk_overlap,
            sperators=['\n\n', '\n', '.', ',']
            )
        
        # 3 Data Vectorization
        if True :#splits_rec:
            vectorizer = Vectorizer(data_splits=splits_rec)
            vector_index_huggingface = vectorizer.build_vectorindex_with_faiss_and_huggingface(model_name=vectorization_config.encoder_name, 
                                                                                            save_to_local=True,
                                                                                            file_dir=vectorization_config.root_dir,
                                                                                            file_name="faiss_Store_huggingface.pkl")
            
  
            st.session_state.url_processed = True
            st.session_state.url_processing = False
        else:
            st.sidebar.markdown(":red[Please check your URLs again]")
            st.session_state.url_processed = False
            st.session_state.url_processing = False      
    
    else:
        st.sidebar.markdown(":red[Please upload URLs first.]")
## Process URLs Ends here

# # Query
if query and st.session_state.url_processed :
    vector_index_huggingface_load = pickel_load(os.path.join(vectorization_config.db_path,"faiss_Store_huggingface.pkl"))
      
    chain = RetrievalQAWithSourcesChain.from_llm(llm=llm, retriever=vector_index_huggingface_load.as_retriever())
    result = chain({"question": query}, return_only_outputs=True)
    # result will be a dictionary of this format --> {"answer": "", "sources": [] }
    st.text_area("Answer",result["answer"])

    # Display sources, if available
    sources = result.get("sources", "")
    if sources:
        st.subheader("Sources:")
        sources_list = sources.split("\n")  # Split the sources by newline
        for source in sources_list:
            st.write(source)

else:
    st.markdown(":red[Please upload and process URLs first.]")
# # Query Ends Here




