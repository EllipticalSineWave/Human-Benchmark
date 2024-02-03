import pyautogui
from PIL import Image
import time  # Import time for optional sleep between iterations

def find_color_and_click(rgb_color):
    while True:
        found = False

        # Take a screenshot
        screenshot = pyautogui.screenshot()

        # Convert screenshot to a PIL Image for easier processing
        img = screenshot.convert('RGB')
        width, height = img.size

        # Define search area limits
        left, top = 20, 200  # Start of search area
        right, bottom = 1800, 520  # End of search area

        # Iterate over the specified range of the screen
        for x in range(left, right):
            for y in range(top, bottom):
                pixel = img.getpixel((x, y))
                if pixel == rgb_color:
                    pyautogui.click(x, y)  # Click where the color is found
                    found = True
                    print(f"Color found and clicked at ({x}, {y})")
                    time.sleep(.1)  # Sleep a bit to prevent too rapid clicking
                    break  # Break the inner loop
            if found:
                break  # Break the outer loop if color is found

        if not found:
            print("Color not found in this attempt.")

        # Optional: Sleep a bit before the next attempt to reduce CPU usage
        # time.sleep(1)  # Wait for 1 second before next attempt

        if found:  # If you want to stop after the first successful click, uncomment this block
            #break  # This will exit the while loop after the first successful click
            pass

if __name__ == '__main__':
    target_rgb = (136, 195, 239)  # The RGB color we're looking for
    find_color_and_click(target_rgb)
