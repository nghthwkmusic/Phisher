import json

def save_configuration(voice_id, config_file="config.json"):
    with open(config_file, "w") as file:
        json.dump({"voice_id": voice_id}, file)
