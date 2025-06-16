import datasets
from typing import List
from langchain.docstore.document import Document
from smolagents import Tool
from langchain_community.retrievers import BM25Retriever


def generate_docs() -> List[Document]:
    guest_dataset = datasets.load_dataset("agents-course/unit3-invitees", split="train")
    docs = [
        Document(
            page_content="\n".join(
                [
                    f"Name: {guest['name']}",
                    f"Relationship: {guest['relation']}",
                    f"Description: {guest['description']}",
                    f"Email: {guest['email']}",
                ]
            ),
            metadata={
                "name": guest["name"],
            }
        )
        for guest in guest_dataset
    ]
    return docs


class GuestInfoRetrieverTool(Tool):
    name = "guest_info_retriever"
    description = "Retrieves detailed information about gala guests based on their name or relation."
    inputs = {
        "query": {
            "type": "string",
            "description": "The name or relation of the guest you want information about."
        }
    }
    output_type = "string"
    
    def __init__(self, docs: List[Document]):
        self.is_initialized = False
        self.retriever = BM25Retriever.from_documents(docs)
        
    def forward(self, query: str) -> str:
        results = self.retriever.get_relevant_documents(query)
        if results:
            return "\n\n".join(
                [
                    doc.page_content
                    for doc in results[:3]
                ]
            )
        else:
            return "No matching guest information found."
        