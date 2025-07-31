from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

model = ChatOpenAI(model="gpt-4")

def summarize_files(files_data,repo_tree):

    prompt = PromptTemplate(
    template ="""
    You are a helpful GitHub codebase summarizer.

    You are given:
    - A set of code files and their contents
    - The folder structure of the repository

    Your task is to extract and summarize **only the most relevant and meaningful information** from the codebase to assist future tools in understanding it better. You are NOT generating actual files like README or requirements.txt — you are just **surfacing useful signals** from the codebase.

    Focus on:
    1. Main purposes of the codebase and key modules/components.
    2. Function and class names, along with a short description of their purpose and any important logic or interaction.
    3. Grouped imports that are **external libraries** (for estimating requirements) and this is strict constraint to add all imports in summary.
    4. Any configuration, routing, data models, or patterns (e.g., MVC, API routes, database schemas) that define project structure.
    5. Use the folder structure to hint at responsibilities or separation of concerns.
    6. Skip minor functions, repetitive boilerplate, and large code blocks.

    Goal: Make it easier for a follow-up LLM agent to answer questions, extract documentation, or perform reasoning using this summarized view.

    Input Files:
    {files_data}

    Repo Tree:
    {repo_tree}

    Now, provide a concise and useful summary:
    """,
        input_variables=['files_data','repo_tree']
    )

    parser = StrOutputParser()

    chain = prompt | model | parser
    response = chain.invoke({'files_data':files_data,
                             'repo_tree':repo_tree}) 
    return response

