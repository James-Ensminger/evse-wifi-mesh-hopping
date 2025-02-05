import csv
import re

def parse_file(path, csv_file, evse_model):
    evse = evse_model
    with open(f"{path}\\{csv_file}", 'r') as file:
        reader = csv.reader(file)

        hop_count = 0
        hz_change = False
        wap_connected = True
        match = ""
        pattern = [r"WIFI CHANGE FREQUENCY from [0-9]*\.[0-9]+ GHz to [0-9]*\.[0-9]+ GHz",
                   r"WIFI CONNECTED to ([A-Za-z0-9]+(:[A-Za-z0-9]+)+)  [0-9]*\.[0-9]+ GHz"]

        for row in reader:
            match = re.search(pattern[0], row[0])
            if wap_connected and match:
                wap_connected = False
                hz_change = True
            match = re.search(pattern[1], row[0])
            if hz_change and match:
                wap_connected = True
                hz_change = False
                hop_count += 1

    print(f"# of WAP hops ({evse}): {hop_count}")