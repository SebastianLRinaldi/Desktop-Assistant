# does things with user inputs to pass to mapper
# gets user input
# tokenizes it
# passes it to map

# This is from my youtube downloader 
import inspect
from bot_function_to_user_commands_mapper import functions

def execute_user_command():
    # Call the appropriate function based on user choice
    # Get the user's choice
    exit_command_received = False
    while not exit_command_received: 

        # Prompt user to enter a command
        command = input("Enter a command (or 'exit' to quit): ")

        # logic for exit 
        if command.lower() == 'exit':
            exit_command_received = True
        
        # commare user input to names of commands 
        
        elif command in functions:
            #   if there is a match get functions number of args for that function
            selected_function = functions[command]['function']
            num_params = len(inspect.signature(selected_function).parameters) # get number of parameters dynamically
            print(num_params)

            user_parameter = get_input(num_params, command)
            print(user_parameter)
            print(*user_parameter)

            # with function found by user command 
            # and 
            # with args passed in by the user 
            # run the function with those args
            # and show result 
            result = selected_function(*user_parameter)
            print(f"Command Executed: Returns - {result}\n")

        else:
            print("Invalid command")


def get_input(num_params, command):
    inputs = []
    for parameter_index in range(num_params):
        description = functions[command]['description']
        needed_param = functions[command]['needed parameters'][parameter_index]
        # tell user what args they need to give and which ones are optional
        # don't have a built in yet for prompts specifc to commands
        prompt = f"{description}\nEnter {needed_param}:"
        user_input = input(prompt)
        inputs.append(user_input)
    return inputs
