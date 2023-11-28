import requests

ELEVENLABS_API_KEY = 'f153c213864927bff8fd1c68bcc84837'

def add_voice(description, files, labels, name):
    url = "https://api.elevenlabs.io/v1/voices/add"
    headers = {
        "xi-api-key": ELEVENLABS_API_KEY
    }
    data = {
        "description": description,
        "labels": labels,
        "name": name
    }
    files = [("files", (file_name, open(file_name, "rb"), "audio/mpeg")) for file_name in files]
    
    response = requests.post(url, headers=headers, data=data, files=files)
    return response.json()

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
    response = requests.post('https://api.elevenlabs.io/v1/audio', headers=headers, json=request_body)

    # Check for successful response
    if response.status_code == 201:
        # Extract audio URL from response JSON
        audio_url = response.json()['audio_url']
        return audio_url
    else:
        raise Exception(f'Speech synthesis failed: {response.status_code} - {response.text}')
