import fitz  # PyMuPDF
import sys
import os

def pdf_to_png(pdf_path, output_folder="output_images"):
    """
    Convert a PDF file to PNG images.

    Args:
        pdf_path (str): Path to the PDF file.
        output_folder (str): Folder to save the PNG images.
    """
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Open the PDF file
    pdf_document = fitz.open(pdf_path)

    # Iterate through each page
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)  # Load the page
        zoom = 2  # Increase this for higher resolution
        mat = fitz.Matrix(zoom, zoom)  # Create a transformation matrix
        pix = page.get_pixmap(matrix=mat)  # Render page to an image

        # Save the image as PNG
        output_path = os.path.join(output_folder, f"page_{page_num + 1}.png")
        pix.save(output_path)
        print(f"Saved: {output_path}")

    print("Conversion complete!")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python pdf_to_png.py <path_to_pdf_file>")
    else:
        pdf_path = sys.argv[1]
        pdf_to_png(pdf_path)