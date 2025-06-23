# youtube_downloader.py

import os
from pytube import YouTube

def download_video(url):
    try:
        yt = YouTube(url)
        print(f"Downloading: {yt.title}")
        stream = yt.streams.get_highest_resolution()
        stream.download()
        print("✅ Download complete!")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    video_url = input("Enter YouTube video URL: ")
    download_video(video_url)