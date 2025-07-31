from langchain_together import ChatTogether
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()


llm = ChatTogether(
    model="deepseek-ai/DeepSeek-V3"
)

def readme_generator(summarized_data_of_repo:str,repo_tree):
    prompt = PromptTemplate(
    template="""You are a helpful and professional technical writer.

    Your task is to generate a detailed and well-formatted `README.md` file for a GitHub project. You are provided with:
    - A high-level summary of the codebase and its core logic
    - The folder and file structure of the repository (repo tree)

    Follow these instructions carefully:

    ---

    ### 📄 README Structure

    1. **Project Title** – Derive it from the repo or folder name if not explicitly provided.
    2. **Description** – A brief, compelling overview of what the project does and its purpose.
    3. **Features** – List of major functionalities or highlights of the system.
    4. **Tech Stack** – Technologies, languages, and frameworks used (infer from imports or folder structure).
    5. **Installation Guide** – Step-by-step instructions to install dependencies and run the project.
    6. **Usage** – How to use or interact with the system, including examples if appropriate (e.g., API calls, CLI usage).
    7. **Folder Structure** – Present the repo tree in a code block and describe each major folder/file briefly.
    8. **Contributing** – (Optional) Add generic guidelines for contributions.
    9. **License** – Leave a placeholder or infer if it's present in the tree.

    ---

    ### 🧠 Content Summary

    Use the `summary` input to extract meaningful function names, library usage, core logic, and purpose of files. Do not copy code. Instead, explain what matters to a new developer or user.

    Avoid verbose technical jargon. Keep it clear, beginner-friendly, and informative.

    ---

    ### 📁 Inputs

    #### Summary of Code:
    {summary}

    #### Repo Tree:
    {repo_tree}

    ---

    Now generate a clean, markdown-formatted `README.md` that follows the above structure.
    """,
        input_variables=['summary','repo_tree']
    )
    parser = StrOutputParser()
    chain = prompt | llm | parser

    response = chain.invoke({'summary':summarized_data_of_repo,
                             'repo_tree':repo_tree})
    return response

