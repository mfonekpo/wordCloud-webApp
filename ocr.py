from PIL import Image
import io
from pytesseract import image_to_string
imagefile = "./1.png"

def perform_ocr_on_image(image_data: bytes) -> str:
    image = Image.open(io.BytesIO(image_data))
    extracted_text = image_to_string(image)
    return extracted_text



if __name__ == "__main__":
    pass

# def perform_ocr_on_image_file(image_file_path: str) -> str:
#     image = Image.open(image_file_path)
#     extracted_text = image_to_string(image)
#     return extracted_text

# imagefile = "./1.png"
# print(perform_ocr_on_image_file(imagefile))
