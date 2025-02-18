import os
import liteon_log_parser

# Grab user input of test time frame in 24hr format
def get_input(user_input_list):
    user_input_list.append(input("Enter start time of test in 24hr format (hh:mm): "))
    user_input_list.append(input("Enter end time of test in 24hr format (hh:mm): "))
    user_input_list.append(input("Enter date of test (mm:dd): "))
    print("---------------------------")
    return user_input_list

# Find charger's log and parse it
path = os.path.join(os.getcwd(), "logs")
user_input = []
for filename in os.listdir(path):
    if filename.__contains__("SC48") and filename.endswith(".csv"):
        print(f'"{filename}" is loading...')
        get_input(user_input)
        liteon_log_parser.parse_file(path, filename, "SC48", user_input)
    elif filename.__contains__("SC48_POS") and filename.endswith(".csv"):
        print(f'"{filename}" is loading...')
        get_input(user_input)
        liteon_log_parser.parse_file(path, filename, "SC48_POS", user_input)
    elif filename.__contains__("IC48") and filename.endswith(".csv"):
        print(f'"{filename}" is loading...')
        get_input(user_input)
        liteon_log_parser.parse_file(path, filename, "IC48", user_input)
    elif filename.__contains__("IC80") and filename.endswith(".csv"):
        print(f'"{filename}" is loading...')
        get_input(user_input)
        liteon_log_parser.parse_file(path, filename, "IC80", user_input)
    user_input.clear()