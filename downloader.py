import yt_dlp

def download_instagram_reel(url):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',  # Ensures highest quality
        'outtmpl': '/content/%(title)s.%(ext)s',  # Sets output file path
        'merge_output_format': 'mp4', 
        'quiet': False,  # Change after tests
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print("📥 Downloading the reel...")
            ydl.download([url])
            print("✅ Download completed successfully!")
    except Exception as e:
        print(f"❌ Error: {e}")

