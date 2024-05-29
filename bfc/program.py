import PyPDF2
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
import io

def add_image_and_text_to_pdf(input_pdf_path, output_pdf_path, image_path, scaling_factor=0.5, image_position=None, text=None, text_position=None, font_path=None):
    """
    Add an image and text to each page of a PDF with optional scaling and manual positioning.
    
    Parameters:
    - input_pdf_path: Path to the input PDF file.
    - output_pdf_path: Path to the output PDF file.
    - image_path: Path to the PNG image file.
    - scaling_factor: Factor to scale the image size (default is 0.5).
    - image_position: Tuple (x, y) for manual positioning of the image. If None, the image is centered (default is None).
    - text: The text to add to the PDF.
    - text_position: Tuple (x, y) for manual positioning of the text. If None, the text is not added.
    - font_path: Path to the custom font file (e.g., OTF or TTF). If None, default font is used.
    """
    # Open the original PDF
    with open(input_pdf_path, 'rb') as input_pdf_file:
        reader = PyPDF2.PdfReader(input_pdf_file, strict=False)
        writer = PyPDF2.PdfWriter()

        # Open the image
        img = Image.open(image_path)
        img_width, img_height = img.size

        # Apply scaling factor to image size
        img_width *= scaling_factor
        img_height *= scaling_factor

        # Register the custom font if provided
        if font_path:
            pdfmetrics.registerFont(TTFont('CustomFont', font_path))

        # Iterate over each page of the original PDF
        for page_num in range(len(reader.pages)):
            original_page = reader.pages[page_num]
            original_page_width = float(original_page.mediabox.width)
            original_page_height = float(original_page.mediabox.height)

            # Determine image position
            if image_position:
                img_x, img_y = image_position
            else:
                # Center the image by default
                img_x = (original_page_width - img_width) / 2.0
                img_y = (original_page_height - img_height) / 2.0
            if img_y < 0:
                img_y = (original_page_height - img_height) / 2.0
            elif img_x < 0:
                img_x = (original_page_width - img_width) / 2.0

            # Create a new PDF with the image and text
            packet = io.BytesIO()
            can = canvas.Canvas(packet, pagesize=(original_page_width, original_page_height))

            # Draw the image
            can.drawImage(ImageReader(image_path), img_x, img_y, width=img_width, height=img_height)
            
            # Draw the text if provided
            if text and text_position:
                text_x, text_y = text_position
                if text_x < 0:

                        text_x = (original_page_width - (len(text) * 16.8)) / 2.0
                elif text_y < 0:
                    text_y = (original_page_height - 12) / 2.0
                
                if font_path:
                    can.setFont('CustomFont', 25)
                can.drawString(text_x, text_y, text)
                
            can.save()

            # Move to the beginning of the StringIO buffer
            packet.seek(0)
            new_pdf = PyPDF2.PdfReader(packet)

            # Merge the new PDF (with the image and text) onto the original PDF
            original_page.merge_page(new_pdf.pages[0])

            # Add the modified page to the writer
            writer.add_page(original_page)

        # Write the modified content to the output PDF
        with open(output_pdf_path, 'wb') as output_pdf_file:
            writer.write(output_pdf_file)

def main():

    branches = [
        "Ahmedabad",
        "Amritsar",
        "Anand",
        "Bangalore",
        "Bareily",
        "Bathinda",
        "Bhopal",
        "Bhubaneswar",
        "Calicut",
        "Chandigarh",
        "Chennai",
        "Cochin N",
        "Cochin",
        "Dehradun",
        "Gurugram",
        "Hoshiarpur",
        "Hyderabad",
        "Indore",
        "Jaipur",
        "Jalandhar",
    
    ]

    input_pdf_path = 'master.pdf'
    output_pdf_path = 'output.pdf'
    image_path = 'image.png'
    scaling_factor = 0.25
    image_position = (-1, 220)  # Centered horizontally, 220 units from the bottom
    text = "DEHRADUN"
    text_position = (-1, 192)  # Position the text at (100, 100)
    font_path = 'MikadoBold.ttf'  # Path to the custom font file

    add_image_and_text_to_pdf(input_pdf_path, output_pdf_path, image_path, scaling_factor, image_position, text, text_position, font_path)

if __name__ == '__main__':
    main()