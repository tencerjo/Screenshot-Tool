# v1.1
# added user-defined time delay after each double-click

import pyautogui
import os
import time
from datetime import datetime
import keyboard

try:
    # Get the number of screenshots from the user
    num_screenshots = int(input("Enter the number of screenshots to take: "))
except ValueError:
    print("Invalid input. Please enter a valid number.")
    exit(1)

try:
    # Get the delay between double-click and screenshot in seconds from the user
    delay_after_double_click = float(input("Enter the number of seconds to wait after double-clicking before taking a screenshot: "))
except ValueError:
    print("Invalid input. Please enter a valid number.")
    exit(1)

def take_screenshot(folder_path):
    # Press Tab and double-click before taking a screenshot
    pyautogui.press('tab')
    pyautogui.doubleClick()
    
    # Wait for user-defined time
    time.sleep(delay_after_double_click)

    # Get the current date and time
    now = datetime.now()
    # Format the date and time string for the screenshot filename
    timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
    
    # Define the file path
    file_path = os.path.join(folder_path, f"screenshot_{timestamp}.png")
    
    # Take the screenshot
    screenshot = pyautogui.screenshot()
    
    # Save the screenshot to the file
    screenshot.save(file_path)
    print(f"Screenshot saved to {file_path}")

def on_esc_pressed(event):
    if event.name == 'esc':
        print("Esc key pressed. Exiting...")
        global exit_flag
        exit_flag = True

if __name__ == "__main__":
    # Get the current date and time for the folder name
    now = datetime.now()
    folder_name = now.strftime("%Y-%m-%d_%H-%M-%S")
    
    # Get the current user's home directory
    home_dir = os.path.expanduser('~')
    
    # Define the folder path
    folder_path = os.path.join(home_dir, "Pictures", "Screenshots", folder_name)
    
    # Create the folder if it doesn't exist
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    print(f"Taking {num_screenshots} screenshots. Press 'Esc' to stop early.")
    
    # Wait for the user to press Enter to start
    input("Press Enter to start taking screenshots...")

    # Register the handler for the Esc key press event
    keyboard.on_press(on_esc_pressed)
    
    exit_flag = False
    
    for i in range(num_screenshots):
        if exit_flag:
            break
        
        # Take a screenshot
        take_screenshot(folder_path)
    
    # Unregister the event handler
    keyboard.unhook_all()
    
    # Infinite pause after Esc is pressed and text is printed
    input("Press Enter to exit...")
