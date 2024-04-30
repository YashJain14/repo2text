# repo2text

`repo2text` is a Python utility designed to convert entire code repositories into text format. This tool is particularly useful for those who want to feed repository contents into large language models like Gemini 1.5, GPT-4, Claude, and others that can process extensive context windows. By turning repositories into plain text, `repo2text` facilitates easy ingestion of codebases into models for tasks such as code analysis, summarization, or other AI-driven evaluations.

## Features

- Clone repositories and convert all files or specific types of files into a single text file.
- Ignore non-essential files like `.git` and `__pycache__`.
- Flexible command-line interface to specify file types.

## Installation

Install `repo2text` using pip:

```bash
pip install repo2text
```

## Usage

After installation, `repo2text` can be used directly from the command line:

To convert all files in a repository:
```bash
repo2text https://github.com/YashJain14/Mini-Twitter
```

To convert only specific file types (e.g., Python files):
```bash
repo2text .py https://github.com/YashJain14/Mini-Twitter
```

## Requirements

- Python 3.6 or higher
- GitPython

## Contributing

Contributions are welcome! If you have suggestions for improvements or bug fixes, please create an issue or pull request.

## License

`repo2text` is released under the MIT License. See the `LICENSE` file for more details.
