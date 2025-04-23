import yt_dlp

def download_instagram_reel(url: str):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': '/content/%(title)s.%(ext)s',
        'merge_output_format': 'mp4',
        'quiet': True, 
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
        return(ydl.prepare_filename(ydl.extract_info(url, download=False)))


