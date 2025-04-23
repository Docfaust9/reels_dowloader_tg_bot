import yt_dlp
import re

def download_instagram_reel(url_input: str):
    url = re.findall(r'https:\/\/www\.instagram\.com\/reel\/.+\/\?igsh=\w*', url_input)[0]
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': '/content/%(title)s.%(ext)s',
        'merge_output_format': 'mp4',
        'quiet': True, 
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
        return(ydl.prepare_filename(ydl.extract_info(url, download=False)))


