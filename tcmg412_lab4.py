import requests
import os
import re


def split_logs(filepath):
    if not os.path.isdir("log_data"):
        os.mkdir("log_data")

    # separate lines by month
    months = {}
    # for each line
    for line in open(filepath, 'r'):

        fileinfo = line.split()
        if len(fileinfo) < 4:
            continue

        # if valid request
        else:
            date = fileinfo[3].split('/')

            # if valid date
            if len(date) > 1:

                # store line in dictionary
                if date[1] not in months.keys():
                    months[date[1]] = line
                else:
                    months[date[1]] += line

    # for each month
    for key in months:
        if "." not in str(key):

            # write to file
            with open(os.sep.join(["log_data", f"{key}.txt"]), 'w') as file:
                file.write(months[key])
                file.close()


def threexx(total_requests, filepath):
    redirect_count = 0.0
    with open(filepath) as file:
        for line in file:
            if re.search('\s*(3\d\d)\s\S+', line):
                redirect_count += 1
    print('The percentage of requests that were redirected elsewhere: {0:.2%}'.format(redirect_count / total_requests))


def fourxx(total_requests, filepath):
    error_count = 0.0
    with open(filepath) as file:
        for line in file:
            if re.search('\s*(4\d\d)\s\S+', line):
                error_count += 1
    print('Percentage of client error (4xx) requests: {0:.2%}'.format(error_count / total_requests))



def request_dates(filepath):

    with open(filepath, 'r') as f:
        data1 = f.read()

    for month in ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]:
        pattern = '.*\[([0-9]+/[' + month + ']+/[0-9]{4}):'
        count = 0
        for match in re.finditer(pattern, data1):
            count += 1
        print(f"Number of requests in {month}: {count}")

def request_freq(filepath):

    d = {}
    total_requests = 0
    for line in open(filepath, 'r'):

        total_requests += 1
        fileinfo = line.split('"')
        if len(fileinfo) < 3:
            continue

        # if valid request
        else:
            f = fileinfo[1].split(" ")
            if not len(f) > 2:
                continue

            else:
                f = f[1]
                if f not in d.keys():
                    d[f] = 1
                else:
                    d[f] += 1

    most_requests = 0
    least_requests = 2
    least_requested_filename = ""
    most_requested_filename = ""
    for key in d.keys():
        if d[key] > most_requests:
            most_requests = d[key]
            most_requested_filename = key

        elif d[key] < least_requests:
            least_requests = d[key]
            least_requested_filename = key

    print(f"The most requested file is {most_requested_filename} with {most_requests} requests.")
    print(f"The least requested file is {least_requested_filename} with {least_requests} requests.")
    return total_requests



filepath = "log_data.txt"

response = requests.get("https://s3.amazonaws.com/tcmg476/http_access_log")
data = response.text

with open(filepath, 'w') as file:
    file.write(data)
    file.close()

request_dates(filepath)
total_requests = request_freq(filepath)
threexx(total_requests, filepath)
fourxx(total_requests, filepath)
split_logs(filepath)

print("done")
