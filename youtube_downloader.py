from moviepy.editor import AudioFileClip
import yt_dlp as youtube_dl

def download_audio(url, start_time, duration, output_filename="downloaded_audio.mp3"):
    # Convert start_time to seconds (if it's in "HH:MM:SS" format) or directly to int/float
    start_seconds = convert_to_seconds(start_time)

    # Ensure duration is an int or float representing seconds
    duration_seconds = int(duration)

    with youtube_dl.YoutubeDL({'format': 'bestaudio'}) as ydl:
        info = ydl.extract_info(url, download=False)
        audio_url = info['url']
        with AudioFileClip(audio_url) as audio:
            # Use the converted time values
            audio_clip = audio.subclip(start_seconds, start_seconds + duration_seconds)
            audio_clip.write_audiofile(output_filename)
            

def convert_to_seconds(time_str):
    # Convert "HH:MM:SS" format to seconds
    h, m, s = map(int, time_str.split(':'))
    return h * 3600 + m * 60 + s
