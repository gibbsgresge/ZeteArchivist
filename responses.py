import json

# Function to load the pledge class data from the JSON file
def load_pledge_data(json_file_path):
    with open(json_file_path, 'r') as file:
        return json.load(file)

# Load the data
# Replace 'path_to_pledge_class_list_corrected.json' with the actual path to your JSON file
pledge_data = load_pledge_data('C:/Users/gibbs/Desktop/Personal Coding/DiscordBot/pledge_class_list_corrected.json')

def get_response(message: str) -> str:
    p_message = message.strip()

    # Check if the message is a command to fetch a pledge class
    if p_message.startswith('/'):
        class_name = p_message[1:]  # Extract class name from command
        if class_name in pledge_data:
            return '\n'.join(pledge_data[class_name])

    
    return 'Oops not a valid command'
