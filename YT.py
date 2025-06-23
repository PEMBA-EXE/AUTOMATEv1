import os

def download_video(url):
    print(f"⬇️ Downloading from: {url}")
    os.system(f"yt-dlp \"{url}\"")

if __name__ == "__main__":
    url = input("Enter YouTube URL: ")
    download_video(url)