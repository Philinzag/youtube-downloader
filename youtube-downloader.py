from pytube import YouTube
from moviepy.video.io.VideoFileClip import VideoFileClip
import os

# Define the YouTube video URL and chapter timestamps
video_url = "Your YouTube Video URL"
chapter_timestamps = {
    "Chapter 1": {"start": "0:00", "end": "2:30"},
    "Chapter 2": {"start": "2:31", "end": "5:00"},
    # Add more chapters and timestamps as needed
}

# Set the download location
download_location = "C:/Path/To/Download/Folder"

# Create the download location folder if it doesn't exist
if not os.path.exists(download_location):
    os.makedirs(download_location)

# Download the YouTube video
yt = YouTube(video_url)
video_stream = yt.streams.get_highest_resolution()
video_filename = video_stream.download(output_path=download_location)

# Function to split the video based on chapter timestamps
def split_video(chapter, start_time, end_time):
    video_clip = VideoFileClip(video_filename).subclip(start_time, end_time)
    output_filename = os.path.join(download_location, f"{chapter}.mp4")
    video_clip.write_videofile(output_filename)
    video_clip.close()

# Loop through the chapter timestamps and split the video
for chapter, timestamps in chapter_timestamps.items():
    start_time = timestamps["start"]
    end_time = timestamps["end"]
    split_video(chapter, start_time, end_time)

print("Split and downloaded videos based on chapters!")
