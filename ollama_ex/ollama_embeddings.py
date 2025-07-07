#%% raw
# ollama run deepseek-r1:1.5b
# ollama run llama3.2:1b
import time

from langchain_community.document_loaders import PyPDFLoader
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings
from langchain_ollama import OllamaLLM
from langchain.chains import RetrievalQA

file_path = "../pdf/Resume.pdf"
loader = PyPDFLoader(file_path)
pages = []

for page in loader.lazy_load():
    pages.append(page)


llm = OllamaLLM(model="llama3.2:1b")
embeddings = OllamaEmbeddings(model="llama3.2:1b")

start_time = time.time()
print(f'starting time {start_time}')

vector_store = FAISS.from_documents(pages,embeddings)

def search_resume(query):
    """Search the resume for a specific query."""
    docs = vector_store.similarity_search(query, k=2)
    for doc in docs:
        print(f'Page {doc.metadata["page"]}: {doc.page_content[:300]}\n')

# retrivers = search_resume("What is my name?")



qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=vector_store.as_retriever(),
    return_source_documents=True
)



query = "What is his experience on cncf?"
result = qa_chain.invoke(query)
print(result)
print(f'finished time {time.time() - start_time}')