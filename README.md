# Mister RetrieveRite

Mr. RetrieveRite is a tool based on RAG (Retrieval Augmented Generation), designed for effective, efficient, and high-quality search and text generation.

## Table of Contents

* [Overview](#overview)
  * [Brief Description](#brief-description)
  * [Why ?](#why?)
  * [Technologies Used](#technologies-used)
  * [Target Audience](#target-audience)
  * [Technical Architecture](#technical-rchitecture)
  * [Project Status](#project-status)
  * [Future Plans](#future-plans)
* [Installation](#installation)
* [Usage](#usage)
* [Demo](#demo)
* [Configuration](#configuration)
* [Model and Data](#model-and-data)
* [API Keys and Credentials](#api-keys-and-credentials)
* [Contributing](#contributing)
* [License](#license)
* [Acknowledgments](#acknowledgments)
* [Contact](#contact)


## Overview
### Brief Description

Retrieval-Augmented Generation (RAG) enhances large language models (LLMs) by incorporating external knowledge sources, enabling more informed responses beyond the model's training data. It is a cost-effective approach to improving LLM output so it remains relevant, accurate, and useful in various contexts all without the need to retrain the model.

### Why ?
+ **Challenges to LLMs :** Making things up when it does not have the answer; presenting ou-of-date or generic information. 
+ **Cost-effective implementation :** The computational and financial costs of retraining base models for organization or domain-specific information are high. Aditionally APIs charge for processing tokens. Giving only relevant input to generate a response can be cost efficient.
+ **Current information :** LLMs are trained on a data upto a specific date. RAG allows developers to provide the latest research, statistics, or news to the generative models while maintaining relevancy.
+ **Enhanced user trus :** RAG can provide source attribution. The output includes refrences to sources so the user may cross check.

### Technologies used :
+ Langchain, OpenAI API, Hugging Face, Streamlit, FAISS
+ For this project Langchain and OpenAI API is used for processing data and giving prompts; Hugging Face's transformer model is used to create embeddings; Faiss is used for retrieval; and Streamlit is used to design UI.

### Target Audience :
+ Customer Service Industry
+ Advertising and Marketing
+ Education and E-Learning
+ Healthcare Industry
+ E-commerce and Retail Industry

### Technical Architecture
+ Data Ingestion : Used Langchain's UnstructuredURLLoader class to load data from urls.
+ Split data into chunks : Used langchain's RecursiveCharacterTextSplitter class.
+ Vector DB : Vectorized the chunks using HuggingFaceBgeEmbeddings, create a FAISS vector store using the embeddings and the splits .
+ Retrieval and prompt : Retrieve the relevant chunks from the DB store and formulate an LLM prompt. Used RetrievalQAWithSourcesChain class and OpenAI API.

### Project Status
+ Phase 1 : Currently the project works as a prototype and has the foundational structure to expand on its capabilities to deal with large information database.

### Future Scope
+ Make it more application specific and build different products out of it.
+ Make the data-ingestion system more robust
+ Include a more robust and capable Vector DB  

## Installation
1. Clone this repository to your local machine using:
    ```bash
    $ git clone https://github.com/Palpendiculal/MisterRetriveRite.git
    $ cd your_project
    ```
2. 
