import re
import yt_dlp


def download_instagram_reel(url_input: str):
    url_instagram = re.findall(r'https:\/\/www\.instagram\.com\/reel\/.+\/\?igsh=[^\s]*', url_input)[0]
    url_youtube = re.findall(r'https:\/\/youtube\.com\/shorts\/[^\s]+', url_input)[0]
    url = url_instagram if url_instagram else url_youtube

    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': '/content/%(title)s.%(ext)s',
        'merge_output_format': 'mp4',
        'quiet': True, 
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
        return(ydl.prepare_filename(ydl.extract_info(url, download=False)))

