import PyPDF2
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
import io

def add_image_to_pdf(input_pdf_path, output_pdf_path, image_path, scaling_factor=0.5, position=None):
    """
    Add an image to the center of each page of a PDF with optional scaling and manual positioning.
    
    Parameters:
    - input_pdf_path: Path to the input PDF file.
    - output_pdf_path: Path to the output PDF file.
    - image_path: Path to the PNG image file.
    - scaling_factor: Factor to scale the image size (default is 0.5).
    - position: Tuple (x, y) for manual positioning. If None, the image is centered (default is None).
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

        # Iterate over each page of the original PDF
        for page_num in range(len(reader.pages)):
            original_page = reader.pages[page_num]
            original_page_width = float(original_page.mediabox.width)
            original_page_height = float(original_page.mediabox.height)

            # Determine position (-1 for center)
            if position:
                x, y = position
            else:
                # Center the image by default
                x = (original_page_width - img_width) / 2.0
                y = (original_page_height - img_height) / 2.0
            if y < 0:
                y = (original_page_height - img_height) / 2.0
            elif x < 0:
                x = (original_page_width - img_width) / 2.0

            # Create a new PDF with the image
            packet = io.BytesIO()
            can = canvas.Canvas(packet, pagesize=(original_page_width, original_page_height))
            can.drawImage(ImageReader(image_path), x, y, width=img_width, height=img_height)
            can.save()

            # Move to the beginning of the StringIO buffer
            packet.seek(0)
            new_pdf = PyPDF2.PdfReader(packet)

            # Merge the new PDF (with the image) onto the original PDF
            original_page.merge_page(new_pdf.pages[0])

            # Add the modified page to the writer
            writer.add_page(original_page)

        # Write the modified content to the output PDF
        with open(output_pdf_path, 'wb') as output_pdf_file:
            writer.write(output_pdf_file)

def main(): 
    input_pdf_path = 'dummy.pdf'
    output_pdf_path = 'output.pdf'
    image_path = 'image.png'
    scaling_factor = 0.25
    position = (-1, 220) # Centered horizontally, 220 units from the bottom

    add_image_to_pdf(input_pdf_path, output_pdf_path, image_path, scaling_factor, position)

if __name__ == '__main__':
    main()