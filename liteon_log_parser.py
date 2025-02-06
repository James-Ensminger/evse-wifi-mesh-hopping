import csv
import re
from datetime import datetime, timedelta, timezone

def parse_file(path, csv_file, evse_model, test_time):
    # Convert PST test times to UTC (PST is UTC-8)
    utc_test_time = []
    for time in test_time:
        if time == test_time[2]:
            if "00:" in utc_test_time[0]:
                pst_date = datetime.strptime(time, "%m:%d")
                pst_date = pst_date.replace(year=datetime.now().year)
                utc_date = pst_date + timedelta(days=1)
                utc_test_time.append(utc_date.strftime("%a %b %d"))
                # print(utc_test_time[2])
            else:
                pst_date = datetime.strptime(time, "%m:%d")
                pst_date = pst_date.replace(year=datetime.now().year)
                utc_date = pst_date.astimezone(timezone.utc)
                utc_test_time.append(utc_date.strftime("%a %b %d"))
                # print(utc_test_time[2])
        else:
            time_format = "%H:%M"
            pst_time = datetime.strptime(time, time_format)
            time_difference = timedelta(hours=8)
            utc_time = pst_time + time_difference
            utc_test_time.append(utc_time.strftime(time_format))
            # print(utc_test_time)
        print(utc_test_time)

    with open(f"{path}\\{csv_file}", 'r') as file:
        reader = csv.reader(file)

        hop_count = 0
        in_range = False
        hz_change = False
        wap_connected = True
        pattern = [r"WIFI CHANGE FREQUENCY from [0-9]*\.[0-9]+ GHz to [0-9]*\.[0-9]+ GHz",
                   r"WIFI CONNECTED to ([A-Za-z0-9]+(:[A-Za-z0-9]+)+)  [0-9]*\.[0-9]+ GHz",
                   rf"{utc_test_time[0]}:[0-9]+",    # start time of test
                   rf"{utc_test_time[1]}:[0-9]+",    # end time of test
                   utc_test_time[2]]                 # test date

        for row in reader:
            # if (re.search(pattern[2], row[0]) and re.search(pattern[4], row[0])) or in_range:
            if (re.search(pattern[4], row[0]) and re.search(pattern[2], row[0])) or in_range:
                in_range = True
                if re.search(pattern[3], row[0]):
                    break
                elif wap_connected and re.search(pattern[0], row[0]):
                    wap_connected = False
                    hz_change = True
                elif hz_change and re.search(pattern[1], row[0]):
                    wap_connected = True
                    hz_change = False
                    hop_count += 1

    print(f"# of WAP hops ({evse_model}): {hop_count}")