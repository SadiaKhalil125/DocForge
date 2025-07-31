from langchain_together import ChatTogether
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

llm = ChatTogether(model="deepseek-ai/DeepSeek-V3")

def generate_requirements_txt(summarized_data_of_repo: str) -> str:
    prompt = PromptTemplate(
        input_variables=["summary"],
        template="""
        You are an expert Python developer and package manager assistant.

        Your task is to generate a `requirements.txt` file based on the **imported libraries and frameworks** used in the following summarized Python project:

        ---

        📄 **Summary of Codebase:**
        {summary}

        ---

        ### 🧾 Instructions:

        1. Extract **all external libraries and dependencies** (those that are not part of Python's standard library) from the project summary.
        2. **DO NOT include standard libraries** like `os`, `sys`, `math`, `re`, `datetime`, `json`, etc.
        3. Include **only installable packages** (e.g., `numpy`, `pandas`, `requests`, `flask`, `scikit-learn`, `openai`, `langchain`, etc.)
        4. If a library like `transformers` or `langchain` is mentioned, **infer the correct package name and add it**.
        5. If a version is clearly stated or implied, add it using `==`. Otherwise, skip the version constraint.
        6. Do not include any explanation—only output a valid `requirements.txt` content.

        Now generate the `requirements.txt` file content:
        """
    )

    parser = StrOutputParser()
    chain = prompt | llm | parser

    response = chain.invoke({"summary": summarized_data_of_repo})
    return response
