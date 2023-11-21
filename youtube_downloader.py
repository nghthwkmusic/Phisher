from moviepy.editor import AudioFileClip
import youtube_dl

def download_audio(url, start_time, duration, output_filename="downloaded_audio.mp3"):
    with youtube_dl.YoutubeDL({'format': 'bestaudio'}) as ydl:
        info = ydl.extract_info(url, download=False)
        audio_url = info['url']
        with AudioFileClip(audio_url) as audio:
            audio_clip = audio.subclip(start_time, start_time + duration)
            audio_clip.write_audiofile(output_filename)
