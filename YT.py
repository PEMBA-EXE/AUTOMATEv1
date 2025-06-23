from pytube import YouTube
from urllib.parse import urlparse, parse_qs

def extract_video_id(url):
    if "shorts" in url:
        return url.split("/")[-1].split("?")[0]
    elif "youtu.be" in url:
        return url.split("/")[-1].split("?")[0]
    elif "watch?v=" in url:
        return parse_qs(urlparse(url).query).get("v", [""])[0]
    else:
        return ""

def clean_url(url):
    video_id = extract_video_id(url)
    return f"https://www.youtube.com/watch?v={video_id}" if video_id else None

def download_video(url):
    try:
        url = clean_url(url)
        if not url:
            raise Exception("Invalid URL format.")
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        print(f"Downloading: {yt.title}")
        stream.download()
        print("✅ Download complete!")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    link = input("Enter YouTube URL: ")
    download_video(link)