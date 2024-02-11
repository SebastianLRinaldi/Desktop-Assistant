# Mapping of what the user inputs to what the bot does.
import bot_functions as BF
# import mapper_helpers as MH

# This is the dictionary that maps commands to functions, descriptions, and parameters
functions = {

    'test': {
        'function': BF.test_function,
        'description': "This function downloads multiple playlists",
        'default parameters': ['None'],
        'needed parameters': ['While Loop -will need to type multiple playlist urls']
    },
    # 'SP': {
    #     'function': BF.download_playlist_webm_to_mp3, 
    #     'description': "This function downloads a single playlist",
    #     'default parameters': ['None'],
    #     'needed parameters': ['single playlist url']
    # },
    # 'S': {
    #     'function': BF.single_videoURL_webm_to_mp3_stream_Download, 
    #     'description': "This function downloads a single video",
    #     'default parameters': ['None'],
    #     'needed parameters': ['single video url', "two commands", "three commands"]
    # },

    # 'TXT2URL': {
    #     'function': BF.download_and_convert_urls_from_txt,
    #     'description': "This function downloads and converts URLs from a text file",
    #     'default parameters': ['txt_file'],
    #     'needed parameters': ['txt_file - path to the text file containing the URLs']
    # },

    'HELP': {
        'function': lambda: print_function_descriptions(functions),
        'description': 'This function provides help information',
        'default parameters': ['None'],
        'needed parameters': []
    }
}

def print_function_descriptions(function_dictionary):
    for key, value in function_dictionary.items():
        print(f"{key} - {value['description']}")