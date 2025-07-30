# Project Overview

This project generates a high-quality README.md file for a GitHub repository based on the contents of various files within the project.

## Features

* Automatically discovers and reads code files with specific extensions (`.js`, `.ts`, `.vue`, `.py`, `.json`, `.md`) within a specified directory
* Ignores files and directories specified in a `.fileignore` file (similar to `.gitignore`)
* Limits the total character count of the README file to prevent overload
* Utilizes the Groq API to generate a README file with a conversational AI model (Meta Llama)

## Usage

1. Clone this repository and navigate to the project directory
2. Install required dependencies: `pip install -r requirements.txt`
3. Create a `.env` file with your Groq API key: `GROQ_API_KEY=your_api_key_here`
4. Run the script: `python generate_readme.py`

## Generated README File

The generated README file will be written to the current working directory as `README.md`.

## Code Structure

The code consists of the following modules:

* `get_all_code_files`: discovers and returns a list of code files within a specified directory
* `read_files`: reads the contents of the code files and formats them for inclusion in the README file
* `generate_readme_with_llama`: utilizes the Groq API to generate a README file based on the formatted code contents

## Dependencies

* `groq`: Groq API client library
* `dotenv`: loads environment variables from a `.env` file
* `pathspec`: utility library for working with file paths and ignore patterns

## Contributing

Contributions are welcome! If you'd like to improve this project, please submit a pull request with your changes.