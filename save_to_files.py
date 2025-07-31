# Python function to save text to markdown and txt files
def save_to_files(content: str, base_filename: str = "output"):
    md_filename='' 
    txt_filename = ''

    if(base_filename=="README"):
        md_filename = f"{base_filename}.md"
        with open(md_filename, "w", encoding="utf-8") as md_file:
            md_file.write(content)


    if(base_filename=="requirements"):
        txt_filename = f"{base_filename}.txt"
        with open(txt_filename, "w", encoding="utf-8") as txt_file:
            txt_file.write(content)

    return md_filename, txt_filename
