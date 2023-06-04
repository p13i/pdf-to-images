import os
import sys
from pdf2image import convert_from_path

def pdf_to_images(pdf_path, output_dir):
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Convert PDF to images
    pages = convert_from_path(pdf_path)
    
    # Save each page as an image
    for i, page in enumerate(pages):
        image_path = os.path.join(output_dir, f"page_{i+1}.jpg")
        page.save(image_path, "JPEG")

# Check if the correct number of arguments is provided
if len(sys.argv) != 3:
    print("Usage: python script.py <pdf_file_path> <output_directory>")
    sys.exit(1)

# Extract the command-line arguments
pdf_file = sys.argv[1]
output_directory = sys.argv[2]

# Call the function to convert PDF to images
pdf_to_images(pdf_file, output_directory)

