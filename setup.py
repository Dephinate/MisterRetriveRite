import setuptools

__version__ = "0.0.0"

SRC_REPO = "MisterRetriveRite" # Source repo name
REPO_NAME = "MisterRetriveRite" # Github repo name
AUTHOR_NAME = "Palpendiculal" # Github name
AUTHOR_EMAIL = "varuns.india@gmail.com" # Github email

with open ("README.md", "r", encoding= "utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name= SRC_REPO,
    version= __version__,
    description= "A samll python package for RAG implimentation using langchain, Faiss, and streamlit for NLP applications",
    long_description= long_description,
    
    author= AUTHOR_NAME,
    author_email= AUTHOR_EMAIL,
    
    url= f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}",
    project_urls = {
    "Bug Tracker":f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}/issues",
    },
    packages= setuptools.find_packages(where="src"),
    package_dir= {"":"src"}

)

