import os
import sys
import time
import getpass

# ====== Settings ======
PASSWORD = "1234"  # ← Change this
FACEBOOK_URL = "https://www.facebook.com/YOUR_USERNAME"  # ← Your Facebook
VERSION = "v1.0"
AUTHOR = "Pemba Gurung"
GITHUB = "github.com/pemba-gurung"
DOWNLOAD_FOLDER = os.path.join(os.path.expanduser("~"), "YT DOWNLOAD")
# ======================

def clear_screen():
    os.system("clear" if os.name == "posix" else "cls")

def fancy_intro():
    clear_screen()
    print("\n" + "=" * 50)
    print("🚀 LAUNCHING YT DOWNLOADER".center(50))
    print("=" * 50)
    for i in range(3, 0, -1):
        print(f"⏳ Please wait... {i}")
        time.sleep(0.5)
    clear_screen()

def logo():
    print("=" * 50)
    print("🅈 🅃   🄳 🄾 🅆 🄽 🄻 🄾 🄰 🄳 🄴 🅁".center(50))
    print("=" * 50)
    print(f"👤 Author : {AUTHOR}")
    print(f"🌐 GitHub : {GITHUB}")
    print(f"🛠️  Version: {VERSION}")
    print("=" * 50)

def ask_password():
    for attempt in range(3):
        print()
        pwd = getpass.getpass("🔒 Enter Password to Unlock: ").strip()
        if pwd == PASSWORD:
            print("✅ Access Granted!\n")
            time.sleep(1)
            clear_screen()
            logo()
            return
        else:
            print("❌ Incorrect password.")
    print("🚫 Too many failed attempts. Exiting...")
    sys.exit()

def menu():
    print("\nWhat would you like to do?")
    print("1. 📹 Download Full Video")
    print("2. 🎵 Download Audio Only (MP3)")
    print("3. 📞 Contact Owner")
    print("4. ❌ Exit")
    return input("\nEnter choice (1/2/3/4): ").strip()

def create_folder():
    if not os.path.exists(DOWNLOAD_FOLDER):
        os.makedirs(DOWNLOAD_FOLDER)

def download_video(url):
    print("\n⬇️ Downloading full video...")
    create_folder()
    os.system(f"yt-dlp -P \"{DOWNLOAD_FOLDER}\" \"{url}\"")

def download_audio(url):
    print("\n🎵 Downloading audio as MP3...")
    create_folder()
    os.system(f"yt-dlp -x --audio-format mp3 -P \"{DOWNLOAD_FOLDER}\" \"{url}\"")

def open_facebook():
    print("\n🌐 Opening Facebook contact page...")
    os.system(f"xdg-open \"{FACEBOOK_URL}\"")

def main():
    fancy_intro()
    logo()
    ask_password()
    while True:
        choice = menu()
        if choice == "1":
            url = input("\n🔗 Enter YouTube URL: ").strip()
            download_video(url)
        elif choice == "2":
            url = input("\n🔗 Enter YouTube URL: ").strip()
            download_audio(url)
        elif choice == "3":
            open_facebook()
        elif choice == "4":
            print("\n👋 Exiting. Have a good day!")
            break
        else:
            print("\n⚠️ Invalid option. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()