import requests

ELEVENLABS_API_KEY = 'your_api_key_here'

def create_voice(audio_file_path):
    # Read audio file contents
    with open(audio_file_path, 'rb') as audio_file:
        audio_data = audio_file.read()

    # Prepare API request headers
    headers = {
        'Authorization': f'Bearer {ELEVENLABS_API_KEY}',
        'Content-Type': 'application/octet-stream',
    }

    # Send API POST request to create voice
    response = requests.post('https://api.elevenlabs.io/v2/voices', headers=headers, data=audio_data)

    # Check for successful response
    if response.status_code == 201:
        # Extract voice ID from response JSON
        voice_id = response.json()['id']
        return voice_id
    else:
        raise Exception(f'Voice creation failed: {response.status_code} - {response.text}')

def synthesize_speech(voice_id, text):
    # Prepare API request body
    request_body = {
        'voice_id': voice_id,
        'text': text,
    }

    # Prepare API request headers
    headers = {
        'Authorization': f'Bearer {ELEVENLABS_API_KEY}',
        'Content-Type': 'application/json',
    }

    # Send API POST request to synthesize speech
    response = requests.post('https://api.elevenlabs.io/v2/audio', headers=headers, json=request_body)

    # Check for successful response
    if response.status_code == 201:
        # Extract audio URL from response JSON
        audio_url = response.json()['audio_url']
        return audio_url
    else:
        raise Exception(f'Speech synthesis failed: {response.status_code} - {response.text}')