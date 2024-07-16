# v0.5 
# fix esc press end so message is displayed
# Add counter to start
# Defined and moved screenshot delay to top

import pyautogui
import os
import time
from datetime import datetime
import keyboard


# Delay time for screenshots
# 50 = 5s, checks in 5 seconds (0.1-second intervals)
screenshot_delay = 50


def take_screenshot(folder_path):
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
    try:
        # Get the number of screenshots from the user
        num_screenshots = int(input("Enter the number of screenshots to take: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        exit(1)

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
    
    # Countdown for the initial 2-second delay
    for countdown in range(2, 0, -1):
        print(f"Starting in {countdown} seconds...")
        time.sleep(1)
    
    # Register the handler for the Esc key press event
    keyboard.on_press(on_esc_pressed)
    
    exit_flag = False
    
    for i in range(num_screenshots):
        if exit_flag:
            break
        
        # Take a screenshot
        take_screenshot(folder_path)
        
        # Wait for 5 seconds, checking for the exit flag
        for _ in range(screenshot_delay):  # 50 checks in 5 seconds (0.1-second intervals)
            if exit_flag:
                break
            time.sleep(0.1)
    
    # Unregister the event handler
    keyboard.unhook_all()
    
    # Infinite pause after Esc is pressed and text is printed
    input("Press Enter to exit...")
