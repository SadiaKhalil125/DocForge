import streamlit as st
from data_extractor import repo_loader, get_github_repo_tree, extract_owner_repo
from doc_summarizer import summarize_files
from readme_creator import readme_generator
from requirements_txt_creator import generate_requirements_txt
from save_to_files import save_to_files

st.set_page_config(page_title="Github Repo Summarizer", layout="centered")
st.title("📄 GitHub Repo Summarizer + Downloader")
st.markdown("Generates README + Requirements.txt for your repos")

repo_link = st.text_input("🔗 Enter GitHub Repository URL", placeholder="https://github.com/user/repo")
branch = st.text_input("Enter Branch Name",placeholder="main")

if repo_link and st.button("🔍 Summarize & Generate Files"):
    with st.spinner("Generating files..."):
        
        repo_tree = get_github_repo_tree(repo_link=repo_link,branch=branch, token="YOUR PERSONAL ACCESS TOKEN")
        repo_data = repo_loader(repo_link= repo_link,branch=branch,access_token="YOUR PERSONAL ACCESS TOKEN")
        
        summarized = summarize_files(files_data=repo_data,repo_tree=repo_tree)
        readme = readme_generator(summarized_data_of_repo=summarized, repo_tree=repo_tree)
        requirements = generate_requirements_txt(summarized_data_of_repo=summarized)
        
        # Save files
        save_to_files(readme,"README")
        save_to_files(requirements,"requirements")


        st.success("✅ Files generated successfully!")

        # Download buttons
        col1, col2 = st.columns(2)

        with col1:
            with open("README.md", "rb") as f:
                st.download_button("📥 Download README.md", data=f, file_name="README.md", mime="text/markdown")

        with col2:
            with open("requirements.txt", "rb") as f:
                st.download_button("📥 Download requirements.txt", data=f, file_name="requirements.txt", mime="text/plain")

