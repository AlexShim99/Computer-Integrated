import os
import cv2
import pytesseract
import re

pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

def extract_information_from_image(image_path):
    # Load the image using OpenCV
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Perform OCR using pytesseract
    extracted_text = pytesseract.image_to_string(gray_image)

    # Process the extracted text to extract relevant information
    lines = extracted_text.split('\n')
    invoice_number = ''
    date = ''
    amount = ''

    # Iterate over each line and extract the relevant information
    for line in lines:
        if not invoice_number:
            # Extract invoice number (look for "invoice no" keyword)
            match = re.search(r'(?i)invoice\s*no[\s:]+([a-zA-Z0-9]+)', line)
            if match:
                invoice_number = match.group(1).strip()
        if not date:
            # Extract date (look for "invoice date" keyword)
            match = re.search(r'(?i)invoice\s*date[\s:]+([\w\s]+)', line)
            if match:
                date = match.group(1).strip()
        if not amount:
            # Extract amount (look for "total" or "grand total" keyword and number on the same line)
            if re.search(r'(?i)total|grand total', line):
                words = line.split()
                for word in words:
                    if word.replace('.', '').isdigit():
                        amount = word.strip()

    # Return the extracted information
    return invoice_number, date, amount

# Folder containing invoice images
folder_path = "invoice"  # Update with your folder path

# Iterate over images in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        # Full path of the image file
        image_path = os.path.join(folder_path, filename)

        # Extract information from the image
        invoice_number, date, amount = extract_information_from_image(image_path)

        # Print the extracted information
        print("Invoice Number:", invoice_number)
        print("Date:", date)
        print("Amount: RM", amount)
        print("-------------------------------------")

