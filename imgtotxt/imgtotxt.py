from PIL import Image
import pytesseract
import sys
import os

def is_thai_char(char):
    """
    Check if a character is a Thai character.
    """
    return '\u0e00' <= char <= '\u0e7f'

def remove_thai_spaces(text):
    """
    Remove unwanted spaces between Thai characters.
    """
    cleaned_text = []
    i = 0
    while i < len(text):
        if is_thai_char(text[i]):
            # Add the Thai character
            cleaned_text.append(text[i])
            i += 1
            # Skip any spaces after the Thai character
            while i < len(text) and text[i] == ' ' and is_thai_char(text[i + 1] if i + 1 < len(text) else False):
                i += 1
        else:
            # Add non-Thai characters (including spaces) as-is
            cleaned_text.append(text[i])
            i += 1
    return ''.join(cleaned_text)

def image_to_text(image_path, output_txt_path="output.txt"):
    """
    Extract text from an image (supporting multiple languages) and save it to a text file.
    Remove unwanted spaces between Thai characters.
    """
    try:
        # Open the image using PIL (Pillow)
        img = Image.open(image_path)

        # Use Tesseract to extract text (specify both English and Thai languages)
        custom_config = r'--oem 3 --psm 6 -l eng+tha'  # OCR Engine Mode, Page Segmentation Mode, and multiple languages
        extracted_text = pytesseract.image_to_string(img, config=custom_config)

        # Remove unwanted spaces between Thai characters
        cleaned_text = remove_thai_spaces(extracted_text)

        # Save the cleaned text to a .txt file
        with open(output_txt_path, "w", encoding="utf-8") as text_file:
            text_file.write(cleaned_text)

        print(f"Text extracted and saved to: {output_txt_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python image_to_text.py <path_to_image_file>")
    else:
        image_path = sys.argv[1]
        output_txt_path = os.path.splitext(image_path)[0] + ".txt"  # Save as same name as input image
        image_to_text(image_path, output_txt_path)