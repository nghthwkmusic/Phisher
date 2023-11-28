import yt_dlp

def download_audio(url, timestamp, duration):
    # Convert timestamp to seconds
    hours, minutes, seconds = map(int, timestamp.split(':'))
    start_time = hours * 3600 + minutes * 60 + seconds

    # Configure yt_dlp options
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': 'downloaded_audio.%(ext)s',
        'postprocessor_args': [
            '-ss', str(start_time),
            '-t', str(duration)
        ]
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    return "downloaded_audio.mp3"  # This assumes the file is named 'downloaded_audio.mp3'
