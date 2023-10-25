import tkinter as tk
from tkinter import filedialog
import moviepy.editor as mp
from PIL import Image
import os


root = tk.Tk()
root.withdraw()  # Hide the main window

file_path = filedialog.askopenfilename()

# Load the video file
input_video_path = file_path
video_clip = mp.VideoFileClip(input_video_path)

# Calculate the duration of the video in seconds
video_duration = video_clip.duration

# Define the interval for screenshots in seconds (2.5 minutes = 150 seconds)
screenshot_interval = 150

# Create a directory to store the screenshots
output_directory = 'screenshots'
os.makedirs(output_directory, exist_ok=True)

# Create screenshots at 2.5-minute intervals
for i in range(0, int(video_duration), screenshot_interval):
    time_in_seconds = i
    screenshot = video_clip.get_frame(time_in_seconds)
    
    # Construct the output file path
    output_screenshot_path = os.path.join(output_directory, f'screenshot_{i:04d}.jpg')
    
    # Convert the NumPy array to a Pillow Image and save it
    screenshot_image = Image.fromarray(screenshot)
    screenshot_image.save(output_screenshot_path)

# Close the video clip
video_clip.reader.close()

