from elevenlabs import set_api_key, clone, Voice, VoiceSettings, generate

# Set your ElevenLabs API key
set_api_key('f153c213864927bff8fd1c68bcc84837')

MODEL_ID = 'eleven_monolingual_v1'

def add_voice(name, description, files):
    # Clone a voice using the ElevenLabs API
    cloned_voice = clone(
        name=name,
        description=description,
        files=files
    )
    return cloned_voice

def synthesize_speech(voice_id, text, model_id=MODEL_ID):
    # Synthesize speech using the ElevenLabs API
    audio = generate(
        text=text,
        voice=Voice(
            voice_id=voice_id,
            settings=VoiceSettings(stability=1.0, similarity_boost=1.0, style=0, use_speaker_boost=True)
        ),
        model=model_id
        # Removed output_format parameter as it's not supported
    )
    return audio
