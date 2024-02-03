import pyautogui
from PIL import Image
import time  # Import time for optional sleep between iterations


def find_color_and_click(rgb_color, attempts=10):
    while True:
        found = False

        # Take a screenshot
        screenshot = pyautogui.screenshot()

        # Convert screenshot to a PIL Image for easier processing
        img = screenshot.convert('RGB')
        width, height = img.size

        # Iterate over the top half of the screen
        for x in range(width):
            for y in range(height // 2):  # Only top half
                pixel = img.getpixel((x, y))
                if pixel == rgb_color:
                    pyautogui.click(x, y)  # Click where the color is found
                    found = True
                    print(f"Color found and clicked at ({x}, {y})")
                    time.sleep(.1)
                    pyautogui.click(x, y)  # Click where the color is found
                    break  # Break the inner loop
            if found:
                break  # Break the outer loop if color is found

        if not found:
            print("Color not found in this attempt.")

        # Sleep a bit before the next attempt to reduce CPU usage
##        time.sleep(1)  # Wait for 1 second before next attempt

        if found:  # If you want to stop after the first successful click, uncomment this block
            pass


if __name__ == '__main__':
    target_rgb = (0, 219, 132)  # The RGB color we're looking for
    find_color_and_click(target_rgb)
