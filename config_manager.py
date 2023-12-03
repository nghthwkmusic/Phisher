import json

CONFIG_FILE = "config.json"

def get_configuration():
    try:
        with open(CONFIG_FILE, 'r') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return {}  # Return an empty dictionary if JSON is invalid
    except FileNotFoundError:
        return {}  # Return an empty dictionary if file does not exist

def save_configuration(voice_id, api_key=None):
    config = get_configuration()
    
    if voice_id is not None:
        config['voice_id'] = voice_id
    if api_key is not None:
        config['api_key'] = api_key

    with open(CONFIG_FILE, "w") as file:
        json.dump(config, file)
