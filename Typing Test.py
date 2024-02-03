import easyocr
import numpy as np
from PIL import ImageGrab
import pyautogui
import time


def capture_and_ocr(x1, y1, x2, y2):
    # Capture the specified area of the screen
    screen_area = (x1, y1, x2, y2)
    captured_image = ImageGrab.grab(bbox=screen_area)

    # Convert PIL.Image object to a NumPy array
    captured_image_np = np.array(captured_image)
    captured_image_np = captured_image_np[:, :, ::-1].copy()  # Convert RGB to BGR

    # Initialize EasyOCR Reader
    reader = easyocr.Reader(['en'])  # Assuming English text; add other languages if needed

    # Perform OCR on the captured image
    results = reader.readtext(captured_image_np)

    # Concatenate all the recognized text into one string
    full_text = ' '.join([result[1] for result in results])

    # Remove the unwanted beginning string if it exists
    unwanted_text = "How many words per minute can you type?"
    if full_text.startswith(unwanted_text):
        full_text = full_text[len(unwanted_text):].lstrip()  # Remove it and leading whitespace

    # Type out the recognized text
    # Ensure there's a slight delay to switch to the window where you want to type the text
    time.sleep(2)  # Adjust the delay as needed
    pyautogui.typewrite(full_text)
    print(full_text)


# Define the coordinates of the screen area to capture
x1, y1, x2, y2 = 448, 282, 1500, 600

# Execute the function
capture_and_ocr(x1, y1, x2, y2)
