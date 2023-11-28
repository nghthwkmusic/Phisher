import requests

ELEVENLABS_API_KEY = 'f153c213864927bff8fd1c68bcc84837'
MODEL_ID = 'English v1'

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

def synthesize_speech(voice_id, text, model_id = MODEL_ID, output_format='mp3_44100_128', optimize_streaming_latency=0):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    headers = {
        "xi-api-key": ELEVENLABS_API_KEY,
        "Content-Type": "application/json"
    }
    data = {
        "model_id": model_id,
        "text": text,
        "output_format": output_format,
        "optimize_streaming_latency": optimize_streaming_latency,
        "voice_settings": {
            "similarity_boost": 1.0,  # Set default values or adjust as needed
            "stability": 1.0,
            "style": 0,
            "use_speaker_boost": True
        }
    }

    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        audio_url = response.content
        return audio_url
    else:
        raise Exception(f'Speech synthesis failed: {response.status_code} - {response.text}')
