import os
import liteon_log_parser

path = "C:\\Users\\scripts\\evse-wifi-mesh-hopping\\evse-wifi-mesh-hopping\\logs"
for filename in os.listdir(path):
    if filename.__contains__("SC48") and filename.endswith(".csv"):
        liteon_log_parser.parse_file(path, filename, "SC48")
    elif filename.__contains__("SC48_POS") and filename.endswith(".csv"):
        liteon_log_parser.parse_file(path, filename, "SC48_POS")
    elif filename.__contains__("IC48") and filename.endswith(".csv"):
        liteon_log_parser.parse_file(path, filename, "IC48")
    elif filename.__contains__("IC80") and filename.endswith(".csv"):
        liteon_log_parser.parse_file(path, filename, "IC80")
    else:
        print("No CSV formatted log files found.")
        break