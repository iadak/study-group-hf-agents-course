import os
import pandas as pd
from smolagents import (
    CodeAgent, 
    LiteLLMModel, 
    DuckDuckGoSearchTool, 
    FinalAnswerTool,
    VisitWebpageTool,
    WikipediaSearchTool,
    WebSearchTool,
    tool,
    OpenAIServerModel
)
from langchain_community.document_loaders import ArxivLoader

import requests
import yaml

def fetch_questions():
    DEFAULT_API_URL = "https://agents-course-unit4-scoring.hf.space"
    try:
        response = requests.get(f"{DEFAULT_API_URL}/questions")
        response.raise_for_status()
        questions_data = response.json()
        if not questions_data:
            print("Fetched questions list is empty.")
            return "Fetched questions list is empty or invalid format.", None
        print(f"Fetched {len(questions_data)} questions.")
        return questions_data
    except Exception as e:
        print(f"Error fetching questions: {e}")
        raise e
    
def fetch_file(task_id: str, file_name: str):
    DEFAULT_API_URL = "https://agents-course-unit4-scoring.hf.space"
    try:
        response = requests.get(f"{DEFAULT_API_URL}/files/{task_id}")
        response.raise_for_status()
        with open(f"data/question_files/{file_name}", "wb") as f:
            f.write(response.content)
        file_content = response.content
        return file_content
    except Exception as e:
        print(f"Error fetching file: {e}")
        raise e
    

def submit_answers(answers):
    DEFAULT_API_URL = "https://agents-course-unit4-scoring.hf.space"
    request_payload = {
        "username": "pardeep-singh",
        "agent_code": "test",
        "answers": answers
    }
    try:
        response = requests.post(
            f"{DEFAULT_API_URL}/submit",
            json=json.dumps(request_payload),
            headers={"Content-Type": "application/json"}
        )
        response.raise_for_status()
        json_response = response.json()
        print(f"Response: {json_response}")
        return json_response
    except Exception as e:
        print(f"Error submitting answers: {e}")

@tool
def arxiv_search(query: str) -> str:
    """Search Arxiv for a query and return maximum 3 result.
    Args:
        query: The search query."""
    search_docs = ArxivLoader(query=query, load_max_docs=3).load()
    formatted_search_docs = "\n\n---\n\n".join(
        [
            f'<Document source="{doc.metadata["source"]}" page="{doc.metadata.get("page", "")}"/>\n{doc.page_content[:1000]}\n</Document>'
            for doc in search_docs
        ]
    )
    return {"arxiv_results": formatted_search_docs}

@tool
def read_python_file(file_name: str) -> str:
    """Read a python file and return the content.
    Args:
        file_name: The name of the file to read.
    Returns:
        The content of the file.
    """
    base_path = "data/question_files"
    with open(os.path.join(base_path, file_name), "r") as f:
        return f.read()

@tool
def read_excel_file(file_name: str) -> str:
    """Read an excel file with xlsx extension and return the content.
    Args:
        file_name: The name of the file to handle.
    Returns:
        The content of the file.
    """
    base_path = "data/question_files"
    df = pd.read_excel(os.path.join(base_path, file_name))
    return df.to_string()

@tool
def extract_text_from_image(image_path: str) -> str:
    """
    Extract text from an image using pytesseract (if available).
    
    Args:
        image_path: Path to the image file
        
    Returns:
        Extracted text or error message
    """
    try:
        # Try to import pytesseract
        import pytesseract
        from PIL import Image
        
        # Open the image
        image = Image.open(image_path)
        
        # Extract text
        text = pytesseract.image_to_string(image)
        print(f"Extracted text from image:\n\n{text}")
        return f"Extracted text from image:\n\n{text}"
    except ImportError:
        return "Error: pytesseract is not installed. Please install it with 'pip install pytesseract' and ensure Tesseract OCR is installed on your system."
    except Exception as e:
        return f"Error extracting text from image: {str(e)}"

MODEL_ID = "ollama_chat/qwen2.5-coder:7b"

# model = LiteLLMModel(
#     model_id=MODEL_ID,
#     api_base="http://127.0.0.1:11434",
#     num_ctx=8192,
# )
model = OpenAIServerModel(model_id="gpt-4.1-nano")
MODEL_ID = "openai/gpt-4.1-nano"

with open("system_prompt.yaml", 'r') as stream:
    prompt_templates = yaml.safe_load(stream)

agent = CodeAgent(
    model=model,
    tools=[
        WebSearchTool(),
        VisitWebpageTool(),
        WikipediaSearchTool(),
        arxiv_search,
        FinalAnswerTool(),
        extract_text_from_image,
        #read_python_file,
        #read_excel_file
    ],
    planning_interval=3,
    max_steps=10,
    verbosity_level=-1,
    additional_authorized_imports=[
                "pandas",
                "numpy",
                "requests",
                "os",
                "math",
                "sympy",
                "scipy",
                "markdownify",
                "unicodedata",
                "stat",
                "datetime",
                "random",
                "itertools",
                "statistics",
                "queue",
                "time",
                "collections",
                "re",
            ],
    add_base_tools=True,
    #prompt_templates=prompt_templates,
)
questions = fetch_questions()
answers = []
counter = 0
for index, question in enumerate(questions):
    # print(f"Question {index + 1}: Question Key: {question.keys()}")
    # print(
    #     f"Task ID: {question['task_id']}\n"
    #     f"Question: {question['question']}\n"
    #     f"Level: {question['Level']}\n"
    #     f"File_name: {question['file_name']}"
    # )
    # if not question['file_name']:
    #     continue
    if question['file_name']:
        file_content = fetch_file(question['task_id'], question['file_name'])
        file_path = os.path.join("data/question_files", question['file_name'])
        #print(f"File content: {file_content}")
        answer = agent.run(
                f"""You are a general AI assistant.You can use the provided tools and websearch for finding answers. I will ask you a question and provide you with a file_name. Report your thoughts, and finish your answer. YOUR FINAL ANSWER should be a number OR as few words as possible OR a comma separated list of numbers and/or strings. If you are asked for a number, don't use comma to write your number neither use units such as $ or percent sign unless specified otherwise. If you are asked for a string, don't use articles, neither abbreviations (e.g. for cities), and write the digits in plain text unless specified otherwise. If you are asked for a comma separated list, apply the above rules depending of whether the element to be put in the list is a number or a string.
                question:{question['question']}
                file_path:{file_path}""",
        )
    else:
        answer = agent.run(
                f"""You are a general AI assistant.You can use the provided tools and websearch for finding answers. I will ask you a question. Report your thoughts, and finish your answer. YOUR FINAL ANSWER should be a number OR as few words as possible OR a comma separated list of numbers and/or strings. If you are asked for a number, don't use comma to write your number neither use units such as $ or percent sign unless specified otherwise. If you are asked for a string, don't use articles, neither abbreviations (e.g. for cities), and write the digits in plain text unless specified otherwise. If you are asked for a comma separated list, apply the above rules depending of whether the element to be put in the list is a number or a string.
                Question:{question['question']}""",
        )
    print(f"Task ID: {question['task_id']} \nQuestion: {question['question']} \nAnswer: {answer}")
    print()
    answers.append(
        {
            "task_id": question['task_id'],
            "submitted_answer": answer
        }
    )
import json
with open(f"data/answers_with_prompt_{MODEL_ID.split('/')[-1]}_with_file_content_handling.json", "w") as f:
    json.dump(answers, f, indent=2)
print("Submitting answers...")
submit_answers(answers)
print("Answers submitted successfully")
