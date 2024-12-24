# OpenAction-Tool

This program adds JavaScript to a PDF file using the OpenAction dictionary.

This tool allows you to embed JavaScript into a PDF file, which will be executed when the PDF is opened.
This can be useful for automating tasks or adding interactive features to your PDF documents.

## Requirements
The following is required to use the Python Script.

- Python 3.x
- [PyPDF2](https://pypi.org/project/PyPDF2/) library

## Usage

### Using the Executable

1. Run `OpenActionTool.exe`
2. Follow the program instructions to select the JavaScript file and the PDF file.
3. Specify the save location and file name to save the PDF file.

### Using the Python Script

1. Install the required library.
```
pip install PyPDF2
```

2. Run `OpenActionTool.py`
```
python OpenActionTool.py
```
4. Follow the program instructions to select the JavaScript file and the PDF file.
5. Specify the save location and file name to save the PDF file.

## Caution

- Ensure that the JavaScript code you are embedding is safe and does not contain any malicious content.
- Be aware that some PDF viewers may have restrictions or security settings that prevent JavaScript from executing.
