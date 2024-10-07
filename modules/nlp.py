import yaml

# Load commands from config/settings.yaml
def load_commands():
    with open("config/settings.yaml", "r") as file:
        commands = yaml.safe_load(file)
    return commands

def process_command(command):
    command = command.lower()
    if "turn on lights" in command:
        return "turn_on_lights"
    elif "turn off lights" in command:
        return "turn_off_lights"
    elif "exit" in command:
        return "exit"
    else:
        return "unknown"
