import os
from pytube import YouTube
from moviepy.video.io.VideoFileClip import VideoFileClip

# Define the YouTube video URL and chapter timestamps
VIDEO_URL = "Your YouTube Video URL"
chapter_timestamps = {
    "Chapter 1": {"start": "0:00", "end": "2:30"},
    "Chapter 2": {"start": "2:31", "end": "5:00"},
    # Add more chapters and timestamps as needed
}

# Set the download location
DOWNLOAD_LOCATION = "C:/Path/To/Download/Folder"

# Create the download location folder if it doesn't exist
if not os.path.exists(DOWNLOAD_LOCATION):
    os.makedirs(DOWNLOAD_LOCATION)

# Download the YouTube video
yt = YouTube(VIDEO_URL)
video_stream = yt.streams.get_highest_resolution()
video_filename = video_stream.download(output_path=DOWNLOAD_LOCATION)

# Function to split the video based on chapter timestamps
def split_video(chapter, START_TIME, END_TIME):
    video_clip = VideoFileClip(video_filename).subclip(START_TIME, END_TIME)
    output_filename = os.path.join(DOWNLOAD_LOCATION, f"{chapter}.mp4")
    video_clip.write_videofile(output_filename)
    video_clip.close()

# Loop through the chapter timestamps and split the video
for chapter, timestamps in chapter_timestamps.items():
    START_TIME = timestamps["start"]
    END_TIME = timestamps["end"]
    split_video(chapter, START_TIME, END_TIME)

print("Split and downloaded videos based on chapters!")
