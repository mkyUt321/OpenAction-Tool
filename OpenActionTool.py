import tkinter as tk
from tkinter import filedialog
from PyPDF2 import PdfReader, PdfWriter
from PyPDF2.generic import NameObject, DictionaryObject, TextStringObject

# Print the purpose of the program
print("This program adds JavaScript to a PDF file using the OpenAction dictionary.")

# Create a Tkinter root window and hide it
root = tk.Tk()
root.withdraw()

# Ask the user to select the JavaScript file
print("Please select the JavaScript file.")
js_file_path = filedialog.askopenfilename(title="Select the JavaScript file", filetypes=[("JavaScript files", "*.js")])
if not js_file_path or not js_file_path.endswith(".js"):
    print("No JavaScript file selected. Exiting the program.")
    exit()

# Ask the user to select the PDF file
print("Please select the PDF file.")
pdf_file_path = filedialog.askopenfilename(title="Select the PDF file", filetypes=[("PDF files", "*.pdf")])
if not pdf_file_path or not pdf_file_path.endswith(".pdf"):
    print("No PDF file selected. Exiting the program.")
    exit()

# Read the JavaScript file
with open(js_file_path, "r") as js_file:
    js_code = js_file.read()

# Read the PDF
with open(pdf_file_path, "rb") as input_pdf:
    reader = PdfReader(input_pdf)
    writer = PdfWriter()

    # Copy all pages
    for page_num in range(len(reader.pages)):
        writer.add_page(reader.pages[page_num])

    # Set the JavaScript action
    js_action = DictionaryObject()
    js_action.update({
        NameObject("/S"): NameObject("/JavaScript"),
        NameObject("/JS"): TextStringObject(js_code)
    })

    # Add the JavaScript action to the root object
    writer._root_object.update({
        NameObject("/OpenAction"): js_action
    })

    # Write the PDF
    print("Please select the location to save and name the PDF file.")
    output_pdf_path = filedialog.asksaveasfilename(title="Save the PDF file", defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
    if output_pdf_path:
        with open(output_pdf_path, "wb") as output_pdf:
            writer.write(output_pdf)
            print(f"The PDF file with JavaScript has been saved successfully !!!")
    else:
        print("No output PDF file selected. Exiting the program.")