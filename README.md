# Phisher: Synthetic Voice Tool

Phisher is a command-line tool that allows users to create and use synthetic voices from web based videos.
## Description
This Python application enables the extraction of audio segments from YouTube videos, creation of a synthetic voice based on the extracted audio, and synthesis of speech using the created voice. It's a versatile tool for generating custom voiceovers and synthetic speech.

## Features


- Downloads audio from a specified segment of a YouTube video.

- Creates a realistic clone voice voice using the downloaded audio.

- Synthesizes speech from text using the created synthetic voice.

## Requirements
- Python 3.x

## Installation

  

Ensure you have Python 3.x installed on your system. Install the required modules using the provided `requirements.txt` file:

  

```bash
pip install -r requirements.txt
```
This will install all necessary dependencies, including youtube_downloader, elevenlabs_api, and config_manager.

## Usage

Run the script from the command line with the following arguments:
- -u URL, --url URL     YouTube video URL (required if not using --audio-file)
- -t TIMESTAMP, --timestamp TIMESTAMP
                        Timestamp in the video (format: hh:mm:ss; required if using --url)
- -d DURATION, --duration DURATION
                        Duration to capture from the video in seconds (required if using --url)
- -s SOURCE FILE, --source-file SOURCE FILE
                        Path to an existing audio file (optional, use instead of --url)
- -h, --help            show this help message and exit

## Examples
Running with Youtube as source:
  ```bash
python phisher.py -u <YouTube Video URL> -t <Timestamp> -d <Duration>
```

Running with a source file:
  ```bash
python phisher.py -s <Source File Path>
```

After executing the command, you will be prompted to enter the text you wish the synthetic voice to say. The application will process this input and output a synthesized speech.

## Contributing
Contributions to the Phisher project are welcome. Please read the CONTRIBUTING.md file for guidelines on how to contribute.
  
## License
This project is licensed under the MIT License - see the LICENSE.md file for more details.
