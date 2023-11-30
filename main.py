import os
import argparse
from youtube_downloader import download_audio
from elevenlabs_api import add_voice, synthesize_speech
from config_manager import save_configuration
from elevenlabs import play

def create_directory_if_not_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def parse_args():
    parser = argparse.ArgumentParser(description="Phisher: A tool to create and use synthetic voices from YouTube videos.")
    parser.add_argument("url", help="YouTube video URL")
    parser.add_argument("timestamp", help="Timestamp in the video (format: hh:mm:ss)")
    parser.add_argument("duration", type=int, help="Duration to capture from the video in seconds")
    return parser.parse_args()

def main():
    args = parse_args()
    downloaded_audio_file = download_audio(args.url, args.timestamp, args.duration)

    voice_name = input("Enter the name of the person whose voice this is: ")
    voice_description = input("Provide a description for the voice: ")

    # Clone the voice
    voice_response = add_voice(voice_name, voice_description, [downloaded_audio_file])
    print("Voice Response:", voice_response)

    # Extract the voice_id from the response
    voice_id = getattr(voice_response, 'voice_id', None)
    if voice_id is None:
        raise ValueError("Failed to retrieve voice_id from the response.")

    print("Voice ID:", voice_id)
    save_configuration(voice_id)

    # Create main and sub-directories for storing audio files
    main_folder = "Cloned Audio"
    create_directory_if_not_exists(main_folder)
    voice_folder = os.path.join(main_folder, voice_name.replace(' ', '_'))
    create_directory_if_not_exists(voice_folder)

    # Prompt user for mode selection
    mode = input("Do you want to 'talk' or 'save' the audio? (Enter 'talk' or 'save'): ").strip().lower()

    try:
        while True:
            text_to_say = input("Enter the text you want the voice to say (Ctrl+C to exit): ")
            audio = synthesize_speech(voice_id, text_to_say)

            if mode == "talk":
                play(audio)
            elif mode == "save":
                words = text_to_say.split()[:2]  # Get first two words
                file_name_suffix = "_".join(words) if words else "audio"
                filename = f"{voice_name.replace(' ', '_')}_{file_name_suffix}.mp3"
                file_path = os.path.join(voice_folder, filename)
                with open(file_path, "wb") as file:
                    file.write(audio)
                print(f"Audio saved to {file_path}")
            else:
                print("Invalid mode selected. Please restart and choose 'talk' or 'save'.")
                break

    except KeyboardInterrupt:
        print("\nExiting the program.")
        return

if __name__ == "__main__":
    main()
