# Project README Generator
================================

## Overview
-----------

This project utilizes the Groq API to generate a high-quality README.md file for a GitHub project based on the contents of various files within the project directory.

## Features
------------

* **File Scanning**: The script scans the project directory and its subdirectories to identify relevant files with extensions such as `.js`, `.ts`, `.vue`, `.py`, `.json`, and `.md`.
* **Content Extraction**: It extracts the contents of these files and generates a summary for each file.
* **README Generation**: The summaries are then combined and passed through the Groq API to generate a final README.md file.

## Requirements
---------------

* **Groq API Key**: You need to have a Groq API key stored in a `.env` file as `GROQ_API_KEY`.
* **Python Environment**: The script requires Python with the `groq`, `dotenv`, and `pathspec` libraries installed.

## Usage
---------

### Prerequisites

Before running the script, ensure you have:

* Python installed on your system
* The required libraries installed (`groq`, `python-dotenv`, and `pathspec`)
* A Groq API key

### Steps to Generate README

1. Clone the repository and navigate to the project directory.
2. Install the required libraries using pip:

 ```bash
pip install groq python-dotenv pathspec
```

3. Create a `.env` file with your Groq API key:

 ```makefile
GROQ_API_KEY=your_api_key_here
```

4. Run the script:

 ```bash
python generate_readme.py
```

5. The script will generate a README.md file in the project directory.

## Configuration
--------------

You can modify the following variables in the `generate_readme.py` file to customize the script's behavior:

* `EXTENSIONS`: A list of file extensions to consider.
* `EXCLUDE_DIRS`: A list of directories to exclude from the scan.
* `MAX_TOTAL_CHARS`: The maximum number of characters to extract from files.

## Notes
-------

* This script uses the Groq API to generate the README.md file. Make sure to review the Groq API terms of service and usage guidelines.
* The script assumes that the project directory is the current working directory. If your project directory is different, update the `folder_path` variable accordingly.

## Contributing
------------

Contributions are welcome! If you'd like to contribute to this project, please fork the repository and submit a pull request.

## License
-------

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).