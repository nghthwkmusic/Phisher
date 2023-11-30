import os
import argparse
import random
import textwrap
from youtube_downloader import download_audio
from elevenlabs_api import add_voice, synthesize_speech
from config_manager import save_configuration
from elevenlabs import play
from ascii_arts import ascii_arts  # Import the ASCII arts list
from phish_quotes import phish_quotes  # Import the Phish quotes list

def print_ascii_art_and_quote():
    ascii_art = random.choice(ascii_arts)
    phish_quote = f"\"{random.choice(phish_quotes)}\""
    
    max_width = max(len(line) for line in ascii_art.split('\n'))
    wrapped_quote = textwrap.wrap(phish_quote, width=max_width)

    print("+" + "-" * (max_width + 2) + "+")
    for line in ascii_art.split('\n'):
        print("| " + line.ljust(max_width) + " |")
    print("| " + " " * max_width + " |")
    for line in wrapped_quote:
        print("| " + line.center(max_width) + " |")
    print("+" + "-" * (max_width + 2) + "+")

def create_directory_if_not_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def parse_args():
    parser = argparse.ArgumentParser(description="Phisher: A tool to create and use synthetic voices from YouTube videos.")
    parser.add_argument("-u", "--url", help="YouTube video URL (required if not using --audio-file)")
    parser.add_argument("-t", "--timestamp", help="Timestamp in the video (format: hh:mm:ss; required if using --url)")
    parser.add_argument("-d", "--duration", type=int, help="Duration to capture from the video in seconds (required if using --url)")
    parser.add_argument("-s", "--source-file", help="Path to an existing audio file (optional, use instead of --url)", metavar="SOURCE FILE")
    return parser.parse_args()

def main():
    print_ascii_art_and_quote()
    print("\n")

    args = parse_args()

    # Check if either URL or audio file is provided
    if not args.url and not args.audio_file:
        parser.error("Either --url/-u or --audio-file/-a must be provided.")
    elif args.url and (not args.timestamp or not args.duration):
        parser.error("--timestamp/-t and --duration/-d are required when using --url/-u.")

    if args.url:
        print("Downloading audio from YouTube...\n")
        downloaded_audio_file = download_audio(args.url, args.timestamp, args.duration)
    else:
        downloaded_audio_file = args.audio_file
        if not os.path.exists(downloaded_audio_file):
            raise FileNotFoundError(f"Audio file '{downloaded_audio_file}' not found.")

    voice_name = input("Enter the name of the person whose voice this is: ")
    voice_description = input("Provide a description for the voice: ")
    print("\n")

    print("Cloning the voice... Please wait.\n")
    voice_response = add_voice(voice_name, voice_description, [downloaded_audio_file])
    print("Voice Response:", voice_response)
    print("\n")

    voice_id = getattr(voice_response, 'voice_id', None)
    if voice_id is None:
        raise ValueError("Failed to retrieve voice_id from the response.")

    print("Voice ID:", voice_id)
    save_configuration(voice_id)
    print("\n")

    main_folder = "Cloned Audio"
    create_directory_if_not_exists(main_folder)
    voice_folder = os.path.join(main_folder, voice_name.replace(' ', '_'))
    create_directory_if_not_exists(voice_folder)

    mode = input("Do you want to 'talk' or 'save' the audio? (Enter 'talk' or 'save'): ").strip().lower()
    print("\n")

    try:
        while True:
            text_to_say = input("Enter the text you want the voice to say (Ctrl+C to exit): ")
            print("Generating audio... Please wait.\n")
            audio = synthesize_speech(voice_id, text_to_say)

            if mode == "talk":
                print("Playing audio...\n")
                play(audio)
            elif mode == "save":
                words = text_to_say.split()[:2]
                file_name_suffix = "_".join(words) if words else "audio"
                filename = f"{voice_name.replace(' ', '_')}_{file_name_suffix}.mp3"
                file_path = os.path.join(voice_folder, filename)
                with open(file_path, "wb") as file:
                    file.write(audio)
                print(f"Audio saved to {file_path}\n")
            else:
                print("Invalid mode selected. Please restart and choose 'talk' or 'save'.\n")
                break

    except KeyboardInterrupt:
        print("\nExiting the program.")
        return

if __name__ == "__main__":
    main()
