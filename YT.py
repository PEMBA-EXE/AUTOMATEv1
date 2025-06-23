from pytube import YouTube
from urllib.parse import urlparse, parse_qs

def extract_video_id(url):
    try:
        parsed = urlparse(url)
        if "youtu.be" in parsed.netloc:
            return parsed.path.strip("/")
        elif "shorts" in parsed.path:
            return parsed.path.split("/")[-1]
        elif "watch" in parsed.path:
            return parse_qs(parsed.query).get("v", [""])[0]
    except Exception as e:
        return None

def clean_url(url):
    vid = extract_video_id(url)
    if vid:
        return f"https://www.youtube.com/watch?v={vid}"
    return None

def download_video(url):
    try:
        fixed_url = clean_url(url)
        if not fixed_url:
            raise Exception("⚠️ Could not extract valid video ID.")
        yt = YouTube(fixed_url)
        stream = yt.streams.get_highest_resolution()
        print(f"⬇️ Downloading: {yt.title}")
        stream.download()
        print("✅ Download complete!")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    link = input("Enter YouTube URL: ")
    download_video(link)