import requests
from langchain.document_loaders import GithubFileLoader

def get_github_repo_tree(repo_link, branch="main", token="YOUR PERSONAL ACCESS TOKEN"):
    repo_name = extract_owner_repo(repo_link)
    headers = {"Authorization": f"token {token}"} if token else {}
    url = f"https://api.github.com/repos/{repo_name}/git/trees/{branch}?recursive=1"
    
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    tree = response.json()["tree"]
    file_paths = [item["path"] for item in tree if item["type"] == "blob"]
    return file_paths

def repo_loader(repo_link:str, branch:str,access_token="YOUR PERSONAL ACCESS TOKEN"):
    repo_name = extract_owner_repo(repo_link)
    loader = GithubFileLoader(
    repo=repo_name,  
    branch=branch,  
    access_token= access_token,
    github_api_url="https://api.github.com",
    file_filter=lambda file_path: file_path.endswith((
        # Python files
        ".py", ".pyx", ".pyi",
        
        # Web technologies
        ".html", ".htm", ".css", ".js", ".jsx", ".ts", ".tsx",
       
        # Configuration files
        ".json", ".yaml", ".yml", ".toml", ".ini", ".cfg", ".env",
        
        # Programming languages
        ".cpp", ".c", ".h", ".hpp", ".java", ".kt", ".rs", ".go"
    )), )
    documents = loader.load()
    return documents

def extract_owner_repo(github_url: str) -> str:
    if github_url.endswith(".git"):
        github_url = github_url[:-4]
    return "/".join(github_url.strip("/").split("/")[-2:])
