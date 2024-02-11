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
        command = input("Enter a command (or 'exit' to quit): ")
        if command.lower() == 'exit':
            exit_command_received = True

        elif command in functions:
            selected_function = functions[command]['function']
            num_params = len(inspect.signature(selected_function).parameters) # get number of parameters dynamically
            print(num_params)

            user_parameter = get_input(num_params, command)
            print(user_parameter)
            print(*user_parameter)

            result = selected_function(*user_parameter)
            print(f"Command Executed: Returns - {result}\n")

        else:
            print("Invalid command")


def get_input(num_params, command):
    inputs = []
    for parameter_index in range(num_params):
        description = functions[command]['description']
        needed_param = functions[command]['needed parameters'][parameter_index]
        prompt = f"{description}\nEnter {needed_param}:"
        user_input = input(prompt)
        inputs.append(user_input)
    return inputs
