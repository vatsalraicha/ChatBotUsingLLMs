# REPLACE THIS WITH YOUR CODE
import os
import yaml

def get_apikey():
    """
    Reads API key from a configuration file.

    This function opens a configuration file named "apikeys.yml", reads the API key for OpenAI

    Returns:
    api_key (str): The OpenAI API key.
    """
    
    # Construct the full path to the configuration file
    script_dir = "/usercode/"
    file_path = os.path.join(script_dir, "apikeys.yml")

    with open(file_path, 'r') as yamlfile:
        # Use the yaml library to load the contents of the file
        config = yaml.safe_load(yamlfile)  # safe_load is used to prevent execution of arbitrary functions
        
        # Access the API key
        API_KEY = config['openai']['api_key']
        
    return API_KEY

if __name__ == "__main__":
    print("API_KEY", get_apikey())