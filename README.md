# 📄 DocForge - AI-Powered GitHub Repository Documentation Generator

## 🎯 Project Overview

DocForge is an intelligent documentation generation tool that automatically analyzes GitHub repositories and creates comprehensive README files and requirements.txt files. Built with Streamlit and powered by multiple Large Language Models (LLMs), it provides a user-friendly interface for developers to quickly generate professional documentation for their projects.

## 🧠 Why DeepSeek-V3 and Multi-LLM Architecture?

This project serves as an exploration platform for understanding different LLM capabilities and their specialized strengths:

### **DeepSeek-V3 for Code Understanding**
- **Primary Choice**: DeepSeek-V3 is specifically chosen for its exceptional code comprehension capabilities
- **Code Analysis**: Superior understanding of programming patterns, function relationships, and codebase architecture
- **Technical Writing**: Excellent at generating technical documentation that accurately reflects code functionality
- **Multi-language Support**: Handles Python, JavaScript, HTML, and other programming languages effectively

### **Multi-LLM Strategy**
- **GPT-4 for Summarization**: Used in `doc_summarizer.py` for initial codebase analysis and feature extraction
- **DeepSeek-V3 for Documentation**: Specialized in `readme_creator.py` and `requirements_txt_creator.py` for technical writing
- **Comparative Analysis**: This setup allows us to explore how different models handle various aspects of code understanding and documentation generation

## 🚀 Features

### Core Functionality
- **GitHub Repository Analysis**: Automatically fetches and analyzes repository structure and code
- **Intelligent Documentation Generation**: Creates comprehensive README.md files with proper structure
- **Dependency Detection**: Automatically generates requirements.txt based on imported libraries
- **Multi-Format Support**: Analyzes 30+ common file types including Python, JavaScript, TypeScript, HTML, CSS, C++, Java, Rust, Go, configuration files, and documentation
- **Branch Support**: Works with different repository branches (default: main)

### Technical Capabilities
- **Code Understanding**: Deep analysis of function names, class structures, and code patterns
- **Import Detection**: Identifies external dependencies and standard library usage
- **Project Structure Analysis**: Understands folder organization and file relationships
- **Professional Documentation**: Generates well-formatted, informative README files

## 🏗️ Architecture

### Project Structure
```
DocForge/
├── main.py                    # Streamlit web application interface
├── data_extractor.py          # GitHub API integration and file loading
├── doc_summarizer.py          # GPT-4 powered codebase summarization
├── readme_creator.py          # DeepSeek-V3 powered README generation
├── requirements_txt_creator.py # DeepSeek-V3 powered requirements.txt generation
└── save_to_files.py           # File saving utilities
```

### Workflow
1. **Repository Input**: User provides GitHub repository URL and branch name
2. **Data Extraction**: Fetches repository tree and loads relevant files
3. **Code Analysis**: GPT-4 summarizes codebase structure and functionality
4. **Documentation Generation**: DeepSeek-V3 creates README.md and requirements.txt
5. **File Export**: Downloads generated files to user's system

## 🛠️ Technology Stack

### Core Technologies
- **Streamlit**: Web application framework for user interface
- **LangChain**: LLM orchestration and prompt management
- **GitHub API**: Repository data extraction and file access

### LLM Integration
- **OpenAI GPT-4**: Code summarization and analysis (`doc_summarizer.py`)
- **DeepSeek-V3**: Technical documentation generation (`readme_creator.py`, `requirements_txt_creator.py`)
- **Together AI**: DeepSeek-V3 model hosting and inference

### Dependencies
- `streamlit`: Web application framework
- `langchain`: LLM orchestration
- `langchain-openai`: OpenAI model integration
- `langchain-together`: Together AI model integration
- `requests`: HTTP requests for GitHub API
- `python-dotenv`: Environment variable management

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- GitHub Personal Access Token
- OpenAI API Key
- Together AI API Key

### Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd DocForge
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Environment Configuration**
   Create a `.env` file with your API keys:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   TOGETHER_API_KEY=your_together_api_key_here
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Run the Application**
   ```bash
   streamlit run main.py
   ```

## 🎮 Usage

### Web Interface
1. Open the Streamlit application in your browser
2. Enter a GitHub repository URL (e.g., `https://github.com/user/repo`)
3. Specify the branch name (default: main)
4. Click "Summarize & Generate Files"
5. Download the generated README.md and requirements.txt files

### Example Usage
```
Repository URL: https://github.com/username/my-python-project
Branch: main
```

## 🔧 Configuration

### API Keys Setup
- **GitHub Token**: Required for accessing private repositories and higher rate limits
- **OpenAI API Key**: Used for GPT-4 code summarization
- **Together AI Key**: Required for DeepSeek-V3 model access

### Customization Options
- **File Filtering**: Modify file extensions in `data_extractor.py` to analyze different file types
- **Prompt Templates**: Customize prompts in each module for specific documentation styles
- **Model Selection**: Switch between different LLM providers by modifying model configurations

## 🧪 LLM Exploration Insights

### Model Comparison
This project demonstrates the strengths of different LLMs:

**GPT-4 (Code Summarization)**
- Excellent at understanding code patterns and relationships
- Strong analytical capabilities for complex codebases
- Good at extracting meaningful insights from code

**DeepSeek-V3 (Documentation Generation)**
- Superior code understanding and technical writing
- Better at generating accurate technical documentation
- Stronger grasp of programming concepts and best practices

### Learning Outcomes
- **Prompt Engineering**: Understanding how to craft effective prompts for different tasks
- **Model Selection**: Learning when to use specific models for optimal results
- **LLM Orchestration**: Managing multiple models in a single application
- **Code Analysis**: Exploring how LLMs interpret and understand code

## 🔍 Technical Details

### Code Analysis Process
1. **Repository Tree Extraction**: Fetches complete file structure from GitHub API
2. **File Loading**: Loads relevant files (Python, HTML, Markdown) using LangChain's GithubFileLoader
3. **Content Summarization**: GPT-4 analyzes code content and extracts key information
4. **Documentation Generation**: DeepSeek-V3 creates structured documentation based on analysis

### File Processing
- **Supported Formats**: 30+ common file types including:
  - **Programming Languages**: Python (`.py`, `.pyx`, `.pyi`), JavaScript (`.js`, `.jsx`), TypeScript (`.ts`, `.tsx`), C/C++ (`.cpp`, `.c`, `.h`, `.hpp`), Java (`.java`), Kotlin (`.kt`), Rust (`.rs`), Go (`.go`)
  - **Web Technologies**: HTML (`.html`, `.htm`), CSS (`.css`)
  - **Configuration**: JSON, YAML, TOML, INI, environment files
- **Content Analysis**: Function names, imports, class structures, and code patterns
- **Dependency Detection**: Automatic identification of external libraries across multiple ecosystems

### Error Handling
- GitHub API rate limiting
- Invalid repository URLs
- Missing API keys
- File access permissions

## 🚀 Future Enhancements

### Planned Features
- **Multi-language Support**: Extend to JavaScript, Java, C++, and other languages
- **Custom Templates**: Allow users to define custom README templates
- **Batch Processing**: Process multiple repositories simultaneously
- **Advanced Analysis**: Include code quality metrics and security analysis
- **Integration APIs**: REST API for programmatic access

### LLM Exploration Roadmap
- **Model Benchmarking**: Compare performance across different LLM providers
- **Specialized Models**: Test domain-specific models for different programming languages
- **Fine-tuning**: Explore custom model training for documentation generation
- **Ensemble Methods**: Combine multiple models for improved results

## 🤝 Contributing

We welcome contributions to improve DocForge! Areas for contribution:

- **LLM Integration**: Add support for new models and providers
- **Code Analysis**: Enhance code understanding capabilities
- **Documentation**: Improve README templates and generation quality
- **Testing**: Add comprehensive test coverage
- **Performance**: Optimize processing speed and efficiency

### Development Setup
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- **DeepSeek AI**: For providing the excellent DeepSeek-V3 model
- **OpenAI**: For GPT-4's powerful code analysis capabilities
- **Together AI**: For hosting and providing access to DeepSeek-V3
- **LangChain**: For the excellent LLM orchestration framework
- **Streamlit**: For the intuitive web application framework
