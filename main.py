import argparse
from youtube_downloader import download_audio
from elevenlabs_api import add_voice, synthesize_speech
from config_manager import save_configuration

def parse_args():
    parser = argparse.ArgumentParser(description="Phisher: A tool to create and use synthetic voices from YouTube videos.")
    parser.add_argument("url", help="YouTube video URL")
    parser.add_argument("timestamp", help="Timestamp in the video (format: hh:mm:ss)")
    parser.add_argument("duration", type=int, help="Duration to capture from the video in seconds")
    return parser.parse_args()

def main():
    args = parse_args()

    # Download audio from YouTube
    downloaded_audio_file = download_audio(args.url, args.timestamp, args.duration)

    # Prompt user for voice details
    voice_name = input("Enter the name of the person whose voice this is: ")
    voice_description = input("Provide a description for the voice: ")
    voice_labels = input("Enter labels for the voice (comma-separated): ")

    # Call add_voice with the new parameters
    voice_response = add_voice(voice_description, [downloaded_audio_file], voice_labels, voice_name)
    voice_id = voice_response['id']  # Assuming the response contains an 'id' field
    save_configuration(voice_id)

    text_to_say = input("Enter the text you want the voice to say: ")
    audio_url = synthesize_speech(voice_id, text_to_say)
    # Additional code to handle the download of the synthesized speech

if __name__ == "__main__":
    main()
